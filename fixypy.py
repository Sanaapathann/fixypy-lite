import streamlit as st
import re

def fix_expression(expr):
    expr = re.sub(r'\((\s*\b[a-zA-Z_]+\b\s*)\)', r'("\1")', expr)

    expr = re.sub(r'\b([a-zA-Z_]+)\b\s*\+\s*\b([a-zA-Z_]+)\b', r'"\1" + "\2"', expr)

    expr = re.sub(r'"(.*?)"\s*\+\s*(\d+)', r'"\1" + str(\2)', expr)
    expr = re.sub(r'(\d+)\s*\+\s*"(.*?)"', r'str(\1) + "\2"', expr)

    expr = re.sub(r'\b([a-zA-Z_]+)\b\s*\+\s*(\d+)', r'"\1" + str(\2)', expr)
    expr = re.sub(r'(\d+)\s*\+\s*\b([a-zA-Z_]+)\b', r'str(\1) + "\2"', expr)

    expr = re.sub(r'"(.*?)"\s*-\s*(\d+)', r'"\1"[:-\2]', expr)
    expr = re.sub(r'\b([a-zA-Z_]+)\b\s*-\s*(\d+)', r'"\1"[:-\2]', expr)

    expr = re.sub(r'"(.*?)"\s*/\s*(\d+)', lambda m: f'"{m.group(1)}"[:len("{m.group(1)}")//{m.group(2)}]', expr)
    expr = re.sub(r'\b([a-zA-Z_]+)\b\s*/\s*(\d+)', lambda m: f'"{m.group(1)}"[:len("{m.group(1)}")//{m.group(2)}]', expr)

    expr = re.sub(r'\b([a-zA-Z_]+)\b\s*\*\s*(\d+)', r'"\1" * \2', expr)
    expr = re.sub(r'(\d+)\s*\*\s*\b([a-zA-Z_]+)\b', r'\1 * "\2"', expr)

    return expr

def fixy_suggest(user_input):
    try:
        fixed = fix_expression(user_input)
        if fixed != user_input:
            result = eval(fixed)
            return "suggested", user_input, fixed, result
        else:
            result = eval(user_input)
            return "valid", user_input, None, result
    except Exception as e:
        return "error", user_input, None, str(e)

# --- Streamlit UI ---
st.set_page_config(page_title="FixyPy Lite", page_icon="🐍", layout="centered")

st.title("🐍 FixyPy Lite")
st.caption("Beginner-friendly Python fixer")

st.markdown("""
Ever written `hello + 2` or `word - 1` and Python yelled at you?

**FixyPy Lite** helps turn basic string/math errors into working Python code.
""")

expr = st.text_input(">> Type your Python expression:", placeholder='"hello" - 2')

if st.button("Run"):
    status, original, suggested, result = fixy_suggest(expr)

    if status == "valid":
        st.success(f":) Output: `{result}`")
    elif status == "suggested":
        st.warning(f":| Python didn’t understand this.")
        st.info(f";) Did you mean: `{suggested}`")
        st.success(f":) Output: `{result}`")
    else:
        st.error(f":( Error: `{result}`")

st.markdown("---")
st.markdown("""
>> **Why FixyPy?**  
FixyPy is built for new Python learners. Instead of giving cryptic errors for small mistakes,
it helps you understand what Python expects — like using quotes for strings or converting numbers before combining.

> It’s like having a friendly Python tutor beside you.
""")
