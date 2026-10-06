from talon import Context, Module, actions, settings

ctx = Context()
mod = Module()

@mod.action_class
class UserActions:

    def model_switch():
        """Switches models between conformer and hum"""
        if settings.get("speech.engine") == "wav2letter":
            ctx.settings["speech.engine"] = "Hum (2026-09-20)"
            actions.user.dictation_mode()
            actions.speech.enable()
        elif settings.get("speech.engine") == "Hum (2026-09-20)":
            ctx.settings["speech.engine"] = "wav2letter"
            actions.user.command_mode()
            actions.speech.enable()

    def hum_push_to_talk():
        """Switches models between conformer and hum"""
        if not actions.speech.enabled():
            actions.speech.enable()
        else:
            actions.speech.disable()