# emacs-mode: -*- python-*-
# -*- coding: utf-8 -*-

import Live 
from APCSessionComponent import APCSessionComponent 
from _Framework.ButtonElement import ButtonElement 
from ConfigurableButtonElement import ConfigurableButtonElement #added
class PedaledSessionComponent(APCSessionComponent):
    ' Special SessionComponent with a button (pedal) to fire the selected clip slot '
    __module__ = __name__

    def __init__(self, num_tracks, num_scenes):
        APCSessionComponent.__init__(self, num_tracks, num_scenes)
        self._slot_launch_button = None



    def disconnect(self):
        #for index in range(len(self._tracks_and_listeners)): #added from launchpad
            #track = self._tracks_and_listeners[index][0]
            #listener = self._tracks_and_listeners[index][2]
            #if ((track != None) and track.playing_slot_index_has_listener(listener)):
                #track.remove_playing_slot_index_listener(listener)
        APCSessionComponent.disconnect(self)
        if (self._slot_launch_button != None):
            self._slot_launch_button.remove_value_listener(self._slot_launch_value)
            self._slot_launch_button = None



    def set_slot_launch_button(self, button):
        assert ((button == None) or isinstance(button, ButtonElement))
        if (self._slot_launch_button != button):
            if (self._slot_launch_button != None):
                self._slot_launch_button.remove_value_listener(self._slot_launch_value)
            self._slot_launch_button = button
            if (self._slot_launch_button != None):
                self._slot_launch_button.add_value_listener(self._slot_launch_value)
            self._rebuild_callback()
            self.update()



    def _slot_launch_value(self, value):
        assert (value in range(128))
        assert (self._slot_launch_button != None)
        if self.is_enabled():
            if ((value != 0) or (not self._slot_launch_button.is_momentary())):
                if (self.song().view.highlighted_clip_slot != None):
                    self.song().view.highlighted_clip_slot.fire()



# local variables:
# tab-width: 4

    #def _reassign_tracks(self):
        #for index in range(len(self._tracks_and_listeners)):
            #track = self._tracks_and_listeners[index][0]
            #fire_listener = self._tracks_and_listeners[index][1]
            #playing_listener = self._tracks_and_listeners[index][2]
            #if (track != None):
                #if track.fired_slot_index_has_listener(fire_listener):
                    #track.remove_fired_slot_index_listener(fire_listener)
                #if track.playing_slot_index_has_listener(playing_listener):
                    #track.remove_playing_slot_index_listener(playing_listener)

        #self._tracks_and_listeners = []
        #tracks_to_use = self.tracks_to_use()
        #for index in range(self._num_tracks):
            #fire_listener = lambda index = index:self._on_fired_slot_index_changed(index)

            #playing_listener = lambda index = index:self._on_playing_slot_index_changed(index)

            #track = None
            #if ((self._track_offset + index) < len(tracks_to_use)):
                #track = tracks_to_use[(self._track_offset + index)]
            #if (track != None):
                #self._tracks_and_listeners.append((track,
                 #fire_listener,
                 #playing_listener))
                #track.add_fired_slot_index_listener(fire_listener)
                #track.add_playing_slot_index_listener(playing_listener)
            #self._update_stop_clips_led(index)




    #def _on_fired_slot_index_changed(self, index):
        #self._update_stop_clips_led(index)



    #def _on_playing_slot_index_changed(self, index):
        #self._update_stop_clips_led(index)



    #def _update_stop_clips_led(self, index):
        #if (self.is_enabled() and (self._stop_track_clip_buttons != None)):
            #button = self._stop_track_clip_buttons[index]
            #if (index in range(len(self._tracks_and_listeners))):
                #track = self._tracks_and_listeners[index][0]
                #if (track.fired_slot_index == -2):
                    #button.send_value(self._stop_track_clip_value)
                #elif (track.playing_slot_index >= 0):
                    #button.send_value(1)
                #else:
                    #button.turn_off()
            #else:
                #button.send_value(0)

