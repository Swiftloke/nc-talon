from talon import Context, Module, actions

ctx = Context()
mod = Module()

@mod.action_class
class UserActions:
    def go_up_dir(number: int):
        """pretty obvious"""
        actions.insert(f"cd {"../" * number}")
        # Doesn't work
        # actions.key("return")
        