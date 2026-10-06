history of:
    insert("history | grep \"\"")
    edit.left()

find of:
    insert("find | grep \"\"")
    edit.left()

grep are:
    insert("grep -r \"\" .")
    edit.left()
    edit.left()
    edit.left()

up dir <user.ordinals>:
    user.go_up_dir(ordinals)
    key("enter")
up dir:
    user.go_up_dir(1)
    key("enter")

ls all:
    insert("ls -al")
    key("enter")
ls:
    insert("ls")
    key("enter")

picocom:
    insert("picocom -b 115200 /dev/tty")