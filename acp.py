import subprocess

def executeCommand(cmd):
    print(cmd)
    result = subprocess.run(cmd, shell=True, text=True)
    print(result.stdout if result.stdout else "")
    print("")

executeCommand("git status")
executeCommand("git add -A")
executeCommand("git commit -m 'Update files.'")
executeCommand("git push")