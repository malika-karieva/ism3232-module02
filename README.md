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