import os, sys, re
while True:
    
    os.write(1,("$ ").encode())
    command = input()
    
    if "cd" in command:
        command = command.split("cd")[1].strip()
        try:
            os.chdir(command)
            os.write(1, (os.getcwd() + "\n").encode())
        except FileNotFoundError:
            os.write(1, ("file not found\n").encode())
        
    if "ls" in command:
        print(os.listdir())
    
    if "exit" in command:
        sys.exit(1)
        
    def ForkProcess(rc):
        pid = os.getpid()

        os.write(1, ("About to fork (pid:%d)\n" % pid).encode())

        if rc < 0:
            os.write(2, ("fork failed, returning %d\n" % rc).encode())
            sys.exit(1)
        elif rc == 0:                   # child
            os.write(1, ("I am child.  My pid==%d.  Parent's pid=%d\n" % (os.getpid(), pid)).encode())
        else:                           # parent (forked ok)
            os.write(1, ("I am parent.  My pid=%d.  Child's pid=%d\n" % (pid, rc)).encode())
            
    rc = os.fork()
    ForkProcess(rc)

    


