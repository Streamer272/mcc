# window.py
#
# Copyright 2022 Daniel Svitan
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from gi.repository import Gtk
from .tables import morse_in, morse_out


@Gtk.Template(resource_path='/com/streamer272/MCC/gtk/window.ui')
class MccWindow(Gtk.ApplicationWindow):
    __gtype_name__ = 'MccWindow'

    entry_in = Gtk.Template.Child()
    button_in = Gtk.Template.Child()
    label_in = Gtk.Template.Child()
    entry_out = Gtk.Template.Child()
    button_out = Gtk.Template.Child()
    label_out = Gtk.Template.Child()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.entry_in.connect('activate', lambda _: self.convert(self.entry_in, self.label_in, True))
        self.button_in.connect('clicked', lambda _: self.convert(self.entry_in, self.label_in, True))
        self.entry_out.connect('activate', lambda _: self.convert(self.entry_out, self.label_out, False))
        self.button_out.connect('clicked', lambda _: self.convert(self.entry_out, self.label_out, False))

    def convert(self, entry, label, type_in):
        table = morse_in if type_in else morse_out
        text = entry.get_text().lower()
        result = ""

        for i in text.split(" ") if type_in else text:
            if (i == " "):
                continue

            value = table.get(i)
            if value is None:
                result += "?"
            else:
                result += value
                if not type_in:
                    result += "  "

        label.set_text(result)


class AboutDialog(Gtk.AboutDialog):
    def __init__(self, parent):
        Gtk.AboutDialog.__init__(self)
        self.props.program_name = 'MCC'
        self.props.version = "0.1.0"
        self.props.authors = ['Daniel Svitan']
        self.props.copyright = '2022 Daniel Svitan'
        self.props.logo_icon_name = 'com.streamer272.MCC'
        self.props.modal = True
        self.set_transient_for(parent)

