# IST356 Assignment 01 — Course Workflow Walkthrough

Welcome to your first assignment! This one is **more about *how* to complete an
assignment in this course than it is about Python programming.** Follow it
top-to-bottom: first you'll open the assignment in the course environment
(**Prep**), then you'll walk through the ten things you'll do in *every* assignment
(**Walkthrough**), and finally you'll complete a small graded task and a
reflection (**The Assignment**).

Take your time and don't skip steps — the whole point is to build the muscle
memory for the workflow.

## Meta

### Learning Objectives

By the end of this assignment you will be able to:

1. **Write and edit code** in the VS Code editor
2. **Debug** a program using the VS Code debugger (breakpoints, stepping, variables)
3. **Run automated tests** with pytest using the Testing panel
4. **Run a terminal app** (a plain Python program) and interact with it
5. **Run a notebook app** (a Jupyter `.ipynb` notebook)
6. **Run a Streamlit app** (a web app) in your browser
7. **Commit** your code changes in VS Code
8. **Push** your commits to GitHub
9. **See your code on GitHub** in the browser
10. **Submit your work for grading and review your feedback** using GraderThan

### Assignment Layout

Every assignment in this course shares the same layout:

- `code/` — **where you write code.** Only files in this folder are reviewed for grading.
  - `bill.py` — the **module**: the functions you write (checked by the unit tests)
  - `console.py` — the **console** interface that uses `bill.py`
  - `explore.ipynb` — the **notebook** interface that uses `bill.py`
  - `dashboard.py` — the **Streamlit** interface that uses `bill.py`
  - `reflection.txt` — **where you write your reflection** (graded)
- `tests/` — the automated tests that check your code
  - `test_unit.py` — **Unit Tests** for the functions in `bill.py`
  - `test_integration.py` — **Integration Tests** for the three interfaces
- `grader/` — the autograder used by GraderThan (you don't touch this)
- `.devcontainer/` — configures the pre-built course container (`mafudge/ist356:latest`)
- `.vscode/` — run / debug / test configurations for VS Code
- `.streamlit/` — configuration for the Streamlit app
- `README.md` — these instructions
- `reflection.md` — how to write a good reflection
- `rubric.json` / `requirements.txt` — grading rubric and Python dependencies

### Prerequisites

Before you start, complete the **one-time course setup**:
👉 https://mafudge.github.io/ist356/0-intro/0-0-setup.html

That setup gets your GitHub account ready (and, if you want to work locally, VS Code
and Docker). This assignment runs inside the pre-built course dev container
(`mafudge/ist356:latest`), which already has Python, pytest, Jupyter, and Streamlit
installed — **there is nothing to install manually.**

> **No computer setup? Use GitHub Codespaces** (Prep → Option A) to run everything in
> your browser — you only need a GitHub account.

---

## Prep — Open the assignment

You'll do this at the start of **every** assignment. First fork, then pick **one**
of two ways to open your fork in the course environment.

1. **Fork this repository.** At the top-right of this repo's GitHub page, click
   **Fork**. This makes your own personal copy under your GitHub account. You
   submit and are graded on *your fork*.

Now choose **Option A** (in the browser — nothing to install) **or** **Option B**
(on your own computer). Everything in the Walkthrough works the same either way.

### Option A — GitHub Codespaces (in the browser) ⭐ easiest

A Codespace runs the exact same course container **in the cloud** and opens VS Code
in your browser — there's nothing to install, so this works on a Chromebook, a lab
machine, or a locked-down laptop.

1. Go to **your fork's** page on GitHub. Click the green **Code** button, then the
   **Codespaces** tab.
2. Click **Create codespace on main**. The container builds (the first time takes a
   few minutes).
3. VS Code opens in your browser, already **inside the course container**, with your
   fork's code loaded and Git signed in. You can skip cloning — you're ready.

> Reopen an existing Codespace anytime from **https://github.com/codespaces** (or the
> **Code → Codespaces** tab on your fork). Codespaces have monthly free hours, so
> **stop** yours when you're done: `github.com/codespaces` → **⋯ → Stop codespace**.

### Option B — Your own computer (local dev container)

Requires Docker Desktop and VS Code from the [course setup](https://mafudge.github.io/ist356/0-intro/0-0-setup.html).

1. **Clone your fork.** On your fork's page, click the green **Code** button and copy
   the HTTPS URL, then clone it. Easiest way: in VS Code press `Ctrl+Shift+P` →
   **Git: Clone**, paste the URL, and pick a folder. Or from a terminal:

   ```sh
   git clone https://github.com/YOUR-GITHUB-USERNAME/assignment_01.git
   ```

   > Make sure the URL has **your** username in it, not `ist356`. You cloned the
   > wrong repo if it doesn't.

2. **Open the folder and reopen in the container.** Choose **File → Open Folder** and
   select the cloned `assignment_01` folder. VS Code detects the dev container and
   pops up a notification — click **Reopen in Container**. (If you miss it:
   `Ctrl+Shift+P` → **Dev Containers: Reopen in Container**.) The first build takes a
   few minutes; after that you're working *inside* the course environment.

You're ready. Everything below happens inside VS Code in the course container —
whether that's in your browser (Codespaces) or on your desktop.

---

## Instructions 

In this section you are given assignment instructions. Consider these a checklist for completing the required parts of the assignment.

EXAMPLE: 

- `code/bill.py` complete these functions (`tip_amount`, `grand_total`, `split_evenly`, `is_generous`) and make sure these tests pass (`test_tip_amount`, `test_grand_total`, `test_split_evenly`, `test_split_evenly_rejects_zero_people`, `test_is_generous`).
- complete `code/console.py` get the tip calculator program working.
- complete `code/dashboard.py` get the streamlit calculator program working.
- all tests should pass
- code reflection written

---

## Walkthrough — Do the assignment step by step

This is a guided, hands-on run through the **whole** assignment. Follow it in order.
Each step tells you *what* to do; when you need the *mechanics* ("how do I run a
test?"), follow the link to the matching **Reference — How do I…?** entry below.

Everything happens inside VS Code in the course container — Codespaces or local, it's
identical.

### Step 1 — Write `tip_amount` and run its test

1. Open `code/bill.py` ([Reference #1](#1-how-do-i-write--edit-code)). Find `tip_amount(subtotal, pct)`. Its docstring
   says: return `pct` percent of `subtotal`, rounded to the nearest cent.
2. Write the body:
   ```python
   def tip_amount(subtotal, pct):
       return round(subtotal * pct / 100, 2)
   ```
3. Save (`Ctrl+S`), then run the unit test `test_tip_amount` from the **Testing** panel
   ([Reference #3](#3-how-do-i-run-automated-tests)). You should get a green **✓** — a 20% tip on $50 is $10.00.

### Step 2 — Try your function in the notebook

Open `code/explore.ipynb` and run it ([Reference #5](#5-how-do-i-run-a-notebook-app)). Like the console and Streamlit
apps, the notebook does no math of its own — it `import bill` and calls your functions.
Run the cells top to bottom (`Shift+Enter`, or **Run All**):

1. `import pandas as pd` and `import bill`.
2. One worked example — a $50 bill, 20% tip, split 4 ways — printing the grand total
   and per-person share via `bill.grand_total(...)` and `bill.split_evenly(...)`.
3. A `pandas` table comparing the per-person cost across tip percentages
   `[10, 15, 18, 20, 25]`.
4. A bar chart of that same table.

Change a value — e.g. `subtotal, pct, people = 50.0, 20, 4` in cell 2 — and re-run to
watch the numbers and the chart update. This is a quick way to sanity-check `bill.py`
outside the tests.

### Step 3 — Write `grand_total` *wrong*, then debug it

Learning to read a failing test is the whole point of this step.

1. In `bill.py`, write `grand_total` **incorrectly** on purpose — e.g. return only the
   tip and forget to add the subtotal:
   ```python
   def grand_total(subtotal, pct):
       return tip_amount(subtotal, pct)   # BUG: forgot to add the subtotal
   ```
2. Run `test_grand_total` ([Reference #3](#3-how-do-i-run-automated-tests)). It **fails** — the panel shows something like
   `assert 10.0 == 60.0`.
3. Debug it. In the **Testing** panel, right-click the failing test → **Debug Test**,
   set a breakpoint inside `grand_total`, and use the debugger's **VARIABLES** panel and
   stepping controls ([Reference #2](#2-how-do-i-use-the-vs-code-debugger)) to see that the return value is missing the subtotal.
4. Fix it and re-run until it's green:
   ```python
   def grand_total(subtotal, pct):
       return round(subtotal + tip_amount(subtotal, pct), 2)
   ```

### Step 4 — Write `split_evenly` yourself

Now you try. `split_evenly(total, people)` returns each person's share, rounded to
cents, and must raise `ValueError` when `people` is 0 or less.

Hint: **divide the total by the number of people** and wrap it in `round(..., 2)`. For
the error case, check `if people <= 0:` and `raise ValueError(...)`. Make **both**
`test_split_evenly` and `test_split_evenly_rejects_zero_people` pass ([Reference #3](#3-how-do-i-run-automated-tests)).

<details><summary>Answer — open only if you're stuck</summary>

```python
def split_evenly(total, people):
    if people <= 0:
        raise ValueError("people must be greater than 0")
    return round(total / people, 2)
```
</details>

### Step 5 — Write `is_generous` yourself

`is_generous(pct)` returns `True` when the tip is **20% or more**. Write it and make
`test_is_generous` pass ([Reference #3](#3-how-do-i-run-automated-tests)).

<details><summary>Answer — open only if you're stuck</summary>

```python
def is_generous(pct):
    return pct >= 20
```
</details>

### Step 6 — Commit and push your finished module

Every unit test passes now — save your first checkpoint:

1. Commit with the message `bill.py all tests pass` ([Reference #7](#7-how-do-i-commit-my-changes-in-vs-code)).
2. Push to your fork ([Reference #8](#8-how-do-i-push-my-code-to-github)).
3. View the commit on GitHub ([Reference #9](#9-how-do-i-see-my-code-on-github)).

### Step 7 — Get *early* feedback from GraderThan

You don't have to be finished to get feedback. Submit what you have ([Reference #10](#10-how-do-i-submit-for-grading--and-review-my-feedback--with-graderthan)) and
read the results — you should earn the unit-test points, while the integration and
reflection parts are still incomplete. That's expected.

While you're there, find the **rubric** on the assignment page — it's right above the
submission box, under **"How you'll be graded."** It's the same rubric defined in
`rubric.json`: **10 points total** — Unit Tests (3), Integration Tests (3), Code style &
readability (2), and Reflection (2). Each criterion is also tagged `auto` (graded by the
automated tests) or `ai` (graded by an AI reviewer), so you know what kind of feedback to
expect back (see [Reference #10](#10-how-do-i-submit-for-grading--and-review-my-feedback--with-graderthan)).

### Step 8 — Break `console.py`, then debug it

Time for the console interface. To practice the debugger on a real interface, plant a
logical error or two, run it, watch the integration test fail, and track the bug down.

1. Open `code/console.py` and introduce a logical error — e.g. split the *subtotal*
   instead of the *grand total*:
   ```python
   per_person = split_evenly(subtotal, people)   # BUG: should split `total`
   ```
2. Run `test_console_app` ([Reference #3](#3-how-do-i-run-automated-tests)) — it fails.
3. Run and **debug** `console.py` (Reference [#2](#2-how-do-i-use-the-vs-code-debugger), [#4](#4-how-do-i-run-a-terminal-console-app)): breakpoint the buggy line, inspect
   the variables, and see the per-person amount is wrong.
4. Fix it back to `split_evenly(total, people)` and re-run until `test_console_app`
   passes.

> **Note:** the bug above is one good option (the per-person amount comes out too low
> because it splits the pre-tip subtotal). Swap in a different logical error if you
> prefer — e.g. reversing the `split_evenly(total, people)` arguments.

### Step 9 — "Finish" the assignment (on purpose, incompletely)

Pretend you're done and submit — even though **`dashboard.py` isn't working and the
reflection isn't written.** This is intentional: you're about to see GraderThan catch
what's missing.

### Step 10 — Write a *weak* first reflection

Open `code/reflection.txt` and write a quick, low-effort reflection — the kind
`reflection.md` calls **poor**: vague, no domain terms, not actionable. Something like:

> This assignment was pretty easy. I learned some Python and made the tip calculator
> work. The tests were kind of annoying but I got them to pass. I don't really have any
> questions.

It's not *wrong*, but it's generic (could describe almost any assignment), uses no
terminology, and gives you nothing to act on later. On the rubric that's **0–1 of 2**.

### Step 11 — Commit and push "assignment complete"

Commit with the message `assignment complete`, push, and view it on GitHub
([Reference #7–9](#7-how-do-i-commit-my-changes-in-vs-code)).

### Step 12 — Submit again and read the gaps

Submit to GraderThan ([Reference #10](#10-how-do-i-submit-for-grading--and-review-my-feedback--with-graderthan)). Notice the feedback: **`dashboard.py` still fails
its integration test** and the **reflection scores low.** Good — that's what "not
actually done" looks like.

### Step 13 — Finish `dashboard.py`

Back to work. Complete the Streamlit dashboard and make `test_streamlit_app` pass
(Reference [#3](#3-how-do-i-run-automated-tests), [#6](#6-how-do-i-run-a-streamlit-app)).

<details><summary>Working <code>dashboard.py</code></summary>

```python
import pandas as pd
import streamlit as st

from bill import tip_amount, grand_total, split_evenly, is_generous

st.title("💵 Bill Splitter")

subtotal = st.number_input("Bill subtotal ($)", min_value=0.0, value=50.0, step=1.0, key="subtotal")
pct = st.slider("Tip %", min_value=0, max_value=30, value=18, key="tip")
people = st.number_input("Number of people", min_value=1, value=2, step=1, key="people")

tip = tip_amount(subtotal, pct)
total = grand_total(subtotal, pct)
per_person = split_evenly(total, people)

col1, col2, col3 = st.columns(3)
col1.metric("Tip", f"${tip:.2f}")
col2.metric("Grand total", f"${total:.2f}")
col3.metric("Per person", f"${per_person:.2f}")

if is_generous(pct):
    st.success("That's a generous tip! 🎉")
else:
    st.info("Tip 20% or more to be considered generous.")

st.subheader("Per-person cost by tip %")
percents = [10, 15, 18, 20, 25]
chart = pd.DataFrame(
    {"per person": [split_evenly(grand_total(subtotal, p), people) for p in percents]},
    index=[f"{p}%" for p in percents],
)
st.bar_chart(chart)
```
</details>

### Step 14 — Rewrite the reflection properly

Replace `reflection.txt` with a **good** reflection — specific, using course
terminology (module, interface, unit vs. integration test, breakpoint/debugger), and
actionable (see `reflection.md`). Something like:

> I learned how a **module** (`bill.py`) keeps the logic separate from the three
> **interfaces** (console, notebook, Streamlit) that `import` it — the same four
> functions powered all three. The **unit tests** call each function directly, while the
> **integration tests** run a whole interface; when `test_grand_total` failed I learned
> to read the assertion (expected `60.0`, got `10.0`) instead of guessing. I struggled
> most with the **debugger** — I set a **breakpoint** but forgot I can't edit code while
> the program is paused. Next I want to practice stepping through a failing test and
> reading the **VARIABLES** panel so debugging is my first move, not my last. I also
> want more practice with rounding money (`round(x, 2)`) — I wasn't sure why `100 / 3`
> came out to `33.33`.

Why it scores well (**2 of 2**): it's **specific** (names the exact functions, tests,
and panels), it **uses the terminology** from class (module, interface, unit vs.
integration test, breakpoint, assertion), and it's **actionable** — it names concrete
next steps the student can actually practice.

### Step 15 — Commit the corrected work

Commit `corrected assignment`, push, and view on GitHub ([Reference #7–9](#7-how-do-i-commit-my-changes-in-vs-code)).

### Step 16 — Final submit

Submit to GraderThan one last time ([Reference #10](#10-how-do-i-submit-for-grading--and-review-my-feedback--with-graderthan)). Every test passes and the reflection
scores well — a perfect score. 🎉

---

## Reference — How do I…?

These are the core mechanics you'll use in *every* assignment. The Walkthrough above
links back to them by number.

> **Using GitHub Codespaces (Prep → Option A)?** Every entry below works exactly the
> same — it's the same VS Code and the same course container, just in your browser.
> Only two differ, and each is flagged inline with a 🌐 **In Codespaces** note:
> **running a web app** ([Reference #6](#6-how-do-i-run-a-streamlit-app) — use the **PORTS** panel instead of `localhost`)
> and **pushing to GitHub** ([Reference #8](#8-how-do-i-push-my-code-to-github) — you're already signed in). Menus, panels,
> and keyboard shortcuts are identical.

### 1. How do I write / edit code?

In the **Explorer** (top icon in the Activity Bar on the left, or **View → Explorer**),
open `code/bill.py`. Read the docstrings in the file. Click into the editor, make a
change, and **save** with `Ctrl+S`. That's it — you write and edit all of your code
right here.

### 2. How do I use the VS Code debugger?

The debugger lets you pause a running program and inspect it line-by-line — great
for understanding what your code is actually doing. Here's the mechanic:

1. Open `code/console.py`.
2. **Set a breakpoint:** click just to the **left of a line number** — a red dot
   appears. The program will pause *before* running that line.
3. Start debugging: **Run → Start Debugging** (or press `F5`). Choose
   **Python Debugger: Current File** if prompted.
4. When the program asks for input, type a value in the **TERMINAL** panel and
   press Enter. Execution pauses at your breakpoint.
5. Look at the **VARIABLES** panel (left side) to see the current value of each
   variable.
6. **Step** one line at a time with `F10` (**Run → Step Over**). Watch how the
   variables change.
7. When you're done, **Run → Stop Debugging** (`Shift+F5`).

> You can't edit code while the program is paused — stop debugging first, then edit.

### 3. How do I run automated tests?

Tests tell you whether your code does what it's supposed to.

1. Open the **Testing** panel: **View → Testing** (the beaker/flask icon in the
   Activity Bar).
2. Expand the tree until you can see the individual tests inside
   `tests/test_unit.py` (the **Unit Tests**) and `tests/test_integration.py` (the
   **Integration Tests**).
3. Click the **▶ (play)** button next to a test to run it.
4. A green **✓** means it passed; a red **✗** means it failed. Click a failed test
   to read the **error message** — that's how you learn *what* went wrong.

Run the tests now. They pass once you've finished *The Assignment* — the unit tests
check your `bill.py` functions, and the integration tests check that the console,
notebook, and Streamlit interfaces work.

### 4. How do I run a terminal (console) app?

A "terminal app" is a plain Python program that reads input and prints output in
the terminal.

1. Open `code/console.py`.
2. **Run → Run Without Debugging** (`Ctrl+F5`). Choose **Python Debugger: Current File**
   if asked.
3. The program runs in the **TERMINAL** panel at the bottom. Answer each prompt —
   e.g. `Bill subtotal:` `50`, `Tip percent:` `20`, `Number of people:` `4` — and
   press Enter to see the split.

### 5. How do I run a notebook app?

A Jupyter notebook mixes text and runnable code in "cells."

1. Open `code/explore.ipynb`. It opens in the notebook editor.
2. The first time, click **Select Kernel** (top-right of the notebook) and choose
   the Python interpreter at `/usr/local/bin/python`.
3. Run a single cell with **Shift+Enter**, or click **Run All** at the top to run
   every cell in order.
4. Each code cell's output appears directly beneath it. Follow along with the
   notes inside the notebook.

### 6. How do I run a Streamlit app?

Streamlit turns a Python file into an interactive web app.

1. Open `code/dashboard.py`.
2. Open **Run and Debug** (**View → Run**, the play-with-a-bug icon).
3. From the dropdown at the top, choose **Streamlit Run: Current File**, then press
   the green **▶** button.
4. Open the app in your browser:
   - **On your computer (Option B):** go to **http://localhost:28502** — VS Code
     usually also pops up an **Open in Browser** button on a port notification.
   - 🌐 **In Codespaces (Option A):** `localhost` won't work. Open the **PORTS** tab
     (next to TERMINAL), find port **28502**, and click the 🌐 globe icon (or the
     **Open in Browser** popup) to open the forwarded URL.

   Interact with the tip slider and the number inputs to re-split the bill.
5. Stop it with **Run → Stop Debugging** (`Shift+F5`) when you're done.

### 7. How do I commit my changes in VS Code?

A *commit* is a saved snapshot of your work in git.

1. Open **Source Control**: **View → Source Control** (the branch icon in the
   Activity Bar). You'll see your changed files listed.
2. Hover a file and click **+** to **stage** it (or click **+** on "Changes" to
   stage everything).
3. Type a short **commit message** describing what you did (e.g.
   `Implement bill.py functions`).
4. Click the **✓ Commit** button.

### 8. How do I push my code to GitHub?

Committing saves the snapshot *locally*. **Pushing** sends it to your fork on
GitHub.

- In the **Source Control** panel, click **Sync Changes** (or the **⋯** menu →
  **Push**). If asked to sign in to GitHub, follow the prompts.

  > 🌐 **In Codespaces:** you're already signed in to GitHub, so **Sync Changes**
  > pushes straight to your fork — no sign-in prompt.

### 9. How do I see my code on GitHub?

- In your browser, go to your fork: `https://github.com/YOUR-GITHUB-USERNAME/assignment_01`
  and **refresh**. You should see your latest commit message and your changed
  files. If it's there, your work is safely on GitHub. **This is the copy
  GraderThan reads.**

### 10. How do I submit for grading — and review my feedback — with GraderThan?

GraderThan runs the autograder (unit + integration tests) and an AI reviewer (code
style, reflection) against your fork, then gives you a score and detailed, per-criterion
feedback.

**Submit:**

1. Go to **https://graderthan.cent-su.org** and log in with your SU Microsoft account.
2. On **Your dashboard**, click this assignment.
3. **First time only:** if you see a banner that says **"Link your GitHub account
   first,"** click **Profile** → **Connect GitHub** and authorize it. You only do this
   once — it applies to every assignment all semester.
4. Under **Request grading**, submit your **fork's GitHub URL**
   (e.g. `https://github.com/YOUR-GITHUB-USERNAME/assignment_01`). (Optional) check
   **"Email me when feedback is ready."** Click **Submit for Grading and Feedback.**

> Always **commit and push (steps 7–8) before you submit** — GraderThan only sees
> what's on GitHub. You get multiple attempts, so submit early and often.

**Find the rubric:** every assignment page shows the full rubric right above the
submission box, under **"How you'll be graded."** Each criterion lists its point value
and whether it's graded `auto` (automated tests) or `ai` (AI reviewer) — that's
`rubric.json`, rendered for you.

**Review your feedback:**

1. Scroll to **"Your submissions"** at the bottom of the assignment page and click a
   submission (or find it from your dashboard).
2. The feedback page shows:
   - Your **overall score** (points and %) and status (e.g. **Completed**).
   - A **"What to improve first"** box calling out the top 1–2 things to fix.
   - A **met / partial / missed** summary across criteria, with a **"Show only what
     needs work"** toggle to filter straight to what's costing you points.
   - Each **rubric criterion**, broken out individually — `AUTOMATED` criteria show the
     raw test output (e.g. `3/3 tests passed`); `AI-JUDGED` criteria show a written
     feedback paragraph, the specific lines of your code it flagged (with a one-line
     explanation of the issue), and a **"How to improve"** tip.
3. Fix what's flagged, commit, push, and **submit again** — that's the loop the
   Walkthrough above has you practice (Steps 7, 12, and 16).

---

## The Assignment — what to actually do

You're building a **Bill Splitter**. The pattern is the one you'll use all
semester: write the logic once as functions in a **module**, then reuse it from
several **interfaces**.

### 1. Write the module — `code/bill.py`

`bill.py` holds four small functions. Each has a docstring describing exactly what
it should return:

| function | what it returns |
| --- | --- |
| `tip_amount(subtotal, pct)` | the tip — `pct` percent of `subtotal`, rounded to cents |
| `grand_total(subtotal, pct)` | the subtotal plus the tip |
| `split_evenly(total, people)` | each person's share (and it raises `ValueError` if `people <= 0`) |
| `is_generous(pct)` | `True` when the tip is 20% or more |

Implement them so the **Unit Tests** (`tests/test_unit.py`, [Reference #3](#3-how-do-i-run-automated-tests)) all
pass. These functions do **no** `input()` or `print()` — they just take values in
and return a value out.

### 2. Check the interfaces work

Three interfaces already `import bill` and use your functions — the **Integration
Tests** (`tests/test_integration.py`) confirm each one works once `bill.py` is
correct:

- **`console.py`** — run it ([Reference #4](#4-how-do-i-run-a-terminal-console-app)) and split a bill in the terminal.
- **`explore.ipynb`** — run it ([Reference #5](#5-how-do-i-run-a-notebook-app)) to see the tips compared in a table.
- **`dashboard.py`** — run it ([Reference #6](#6-how-do-i-run-a-streamlit-app)) and split a bill with sliders.

### 3. Reflection

Read `reflection.md`, then write your reflection in **`code/reflection.txt`**. A
good reflection is **specific**, **uses the terminology** from class, and is
**actionable**. This is graded — see `reflection.md` for what "good" looks like.

---

## How You're Graded

GraderThan scores this assignment out of **10 points** (see `rubric.json`):

| What | Points | Judged by |
| --- | --- | --- |
| **Unit Tests** — `test_unit.py` (the `bill.py` functions) | 3 | automated tests |
| **Integration Tests** — `test_integration.py` (the interfaces) | 3 | automated tests |
| Code style & readability | 2 | AI reviewer |
| Reflection quality | 2 | AI reviewer |

**Only files in the `code/` folder are graded.** Commit, push, and submit
([Reference #7–10](#7-how-do-i-commit-my-changes-in-vs-code)) to get your score and feedback.
