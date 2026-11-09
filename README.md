<<<<<<< HEAD
# README.md

Sweet Bakery Order Assistant

This assistant helps bakery customers check the status of their orders using a custom lookup tool. The assistant relies on mock rule-based logic and dictionary lookups rather than a real AI model to respond to messages. Requests involving order cancellations or refunds are handed off to a human manager because the automated system cannot process financial transactions or modify active kitchen tickets. If this assistant used real customer data, a bug or security flaw could expose sensitive personal details like customer phone numbers, home addresses, and payment history to unauthorized users. Additionally, real-time data synchronization errors could cause outdated order statuses to be displayed, leading to customer confusion and delayed pickups.

This assistant combines rule-based logic for order status lookups and human handoffs with a local language model for general questions. The model answered questions about store location and hours well based on its instructions. It refused or stated it did not know when asked about custom cake pricing because that information was outside its provided instruction facts. We decided to keep order tracking and cancellations in Python code rules to ensure exact data lookups and strict security control over financial transactions.
=======
| Command | Description |
|---------|-------------|
| cd | Changes the current directory |
| mkdir | Creates a new directory |
| touch | Creates a new file |
| echo | Displays text |
| cat | Displays file contents |
| head | Displays the first lines of a file |
| tree | Displays the directory structure |
| code | Opens a file or folder in VS Code |

#Week 3 Section: 
cd ~/ism3232/module02_zsh

| Command | Definition |
|---|---|
| `cd ~/ism3232/module02_zsh` | Moves to the module02_zsh folder. |
| `alias ll='ls -la'` | Lists all files with details. |
| `alias py='python3'` | Shortcut for Python 3. |
| `alias gs='git status'` | Shows Git status. |
| `alias ga='git add .'` | Stages all changes. |
| `alias gcmsg='git commit -m'` | Creates a Git commit. |
| `alias gp='git push'` | Pushes changes to GitHub. |
| `alias gl='git log --oneline'` | Shows short commit history. |
| `alias tree2='tree -L 2'` | Shows folders two levels deep. |
| `mkcd() { mkdir -p "$1" && cd "$1"; }` | Creates and enters a folder. |
>>>>>>> 9cfa4b2e3dbf8e81908cefcb0b9782c0b77603fa
