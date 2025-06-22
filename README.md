# 🛠️ FixyPy Lite

**FixyPy Lite** is a beginner-friendly Python sandbox that gently corrects common expression mistakes — like mixing strings and numbers — and suggests what you probably meant.

**Tech Stack**
Python 3.13
Streamlit
Regex & eval-based suggestion engine

Try it now → [https://fixypy.streamlit.app](https://fixypy.streamlit.app)

---

## What is FixyPy Lite?

> `"hello" - 2"` →  error?  
> FixyPy says: `Did you mean: "hello"[:-2]`  Output: `hel`

FixyPy helps new coders learn **by fixing their code** and **explaining the fix** — no cryptic error messages.

It supports:

- `string + string` (`a+a` → `Did you mean "a" + "a"?`)
- `string - number` (`"abc" - 1` → `"abc"[:-1]`)
- `string + number` → suggests type casting
- `number + string` → same fix
- Handles `/`, `-`, `*`, `//` with strings and numbers
- More coming soon!

---

## Why FixyPy Lite is Better for Newbies

- Clear, gentle suggestions instead of scary Python errors
- Tells you what you *meant*, not just what's *wrong*
- Reinforces key Python rules: types, casting, slicing
- Built using Streamlit – no install or login needed
- Perfect for schools, bootcamps, or self-learners

---

## Example Fixes

| Input           | Suggestion                  | Result   |
|----------------|-----------------------------|----------|
| `"a" + "a"`     |  `aa` (works)              | `aa`     |
| `"test" + 5`    | `Did you mean: "test" + str(5)` | `test5` |
| `3 + "b"`       | `Did you mean: str(3) + "b"` | `3b`     |
| `"hello" - 2`   | `Did you mean: "hello"[:-2]` | `hel`    |

---

## How to Use Locally


```bash
git clone https://github.com/Sanaapathann/fixypy-lite.git
cd fixypy-lite
pip install streamlit
streamlit run fixypy.py
