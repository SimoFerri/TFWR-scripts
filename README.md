# The Farmer Was Replaced
Author: Simone Ferri (@SimoFerri)
## 📘 Description
This repository contains the scripts used to progress inside the game
[The farmer was replaced](https://store.steampowered.com/app/2060160/The_Farmer_Was_Replaced/).<br>
- The [Sequential](/Sequential) directory contains scripts that doesn't exploit the parallelism that the *Megafarm* update allows.
- The [Parallel](/Parallel) directory contains scripts that exploit parallelism allowed by the *Megafarm* update.
- The [Leaderboard](/Leaderboard) directory contains scripts used to enter the game leaderboard, each script will come with
a report that explain which choices have been taken and why I took them.



## 🎯 Motivation
This project was created to put into practice the knowledge and techniques I gained during my studies, applying them to a
complex system that simulates real-world behavior.


The main goal is to approach each challenge with a professional and methodical mindset, following a clear and repeatable process:
- **System analysis**: perform a deep understanding of the overall system before implementing any solution.
- **Problem analysis**: break down each issue into well-defined, measurable components.
- **Mathematical modeling**: design mathematical models that accurately describe the core mechanics and constraints of each problem.
- **Solution profiling**: test and profile different approaches to evaluate their efficiency and scalability.
- **Reporting**: create detailed reports summarizing the analysis, models, and results for each problem tackled.<br>

## ⚙️ How to use
To **run the code** you must **copy and paste it inside the game**.<br>
First copy the file `utils.py` inside the root of the project inside the game and rename the window `utils`. Then you can either:
- Copy all the scripts, included `main.py` and run the entire routine. Make sure to rename the windows accordingly the names reported at the beginning of `main.py`.
- Copy only one script and use it inside your projects. Note that each script has a function that starts with `produce_`, call it inside your script to produce the desired resource.

## ⚖️ License
This project is released under the BSD 3-Clause License.  
If you use this code in your own work, please provide proper attribution to **Simone Ferri**.
See the [LICENSE](./LICENSE) file for details.
