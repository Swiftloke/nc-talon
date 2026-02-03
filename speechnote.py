# Unusable version as Talon cannot correctly import GLIB.
# from pydbus import SessionBus
# from gi.repository import GLib
# from talon import Context, actions, settings

# @ctx.action_class("user")
# class UserActions:
#     def speech_note():

#         loop = GLib.MainLoop()
#         bus = SessionBus()

#         r = bus.get("net.mkiol.SpeechNote", "/net/mkiol/SpeechNote")
        
#         def callback():
#             loop.quit()
        
#         r.onStatePropertyChanged = callback
        
#         r.InvokeAction("start-listening-active-window", {})
#         loop.run()

# -*- coding: utf-8 -*-


from talon import actions, settings, Module
import asyncio
from dbus_next.aio import MessageBus
from dbus_next.constants import BusType

mod = Module()

@mod.action_class
class UserActions:
    def speech_note():
        """Executes the SpeechNote command to start listening over Dbus. Blocks Talon until finished listening."""
        def run_async(coro):
            try:
                loop = asyncio.get_running_loop()
            except RuntimeError:
                asyncio.run(coro)
            else:
                fut = asyncio.run_coroutine_threadsafe(coro, loop)
                return fut.result()

        async def _inner():

            bus = await MessageBus(bus_type=BusType.SESSION).connect()

            service_name = "net.mkiol.SpeechNote"
            object_path = "/net/mkiol/SpeechNote"

            introspection = await bus.introspect(service_name, object_path)
            proxy_obj = bus.get_proxy_object(
                service_name,
                object_path,
                introspection,
            )
            iface = proxy_obj.get_interface("net.mkiol.SpeechNote")

            done_fut = asyncio.get_event_loop().create_future()

            def _state_changed_handler(*_args): 
                if not done_fut.done():
                    done_fut.set_result(None)

            iface.on_state_property_changed(_state_changed_handler)

            await iface.call_invoke_action("start-listening-active-window", {})
            await done_fut

        run_async(_inner())
