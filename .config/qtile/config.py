# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from typing import List  # noqa: F401

from libqtile import bar, extension, layout, widget, hook, qtile
from libqtile.config import Click, Drag, Group, Key, KeyChord, Match, Screen
from libqtile.lazy import lazy
from libqtile.command import lazy
from libqtile.utils import guess_terminal

import os
import subprocess

mod = "mod4"
terminal = "alacritty"
browser = "firefox"
home = os.path.expanduser("~")

keys = [
    ### WINDOWS CONTROL -----{{{

    # Switch between windows ---
    #Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    #Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(),
        desc="Move window focus to other window"),

    # Move windows between left/right columns or move up/down in current stack ---
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(),
        desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(),
        desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), lazy.layout.section_down(),
        desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), lazy.layout.section_up(), desc="Move window up"),
    ## ----- ##
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),

    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink ---
    # Note: can't apply to monadtall layout
    Key([mod], "h",
        lazy.layout.shrink(),
        lazy.layout.decrease_nmaster(),
        desc="Grow window to the left"
        ),
    Key([mod], "l",
        lazy.layout.grow(),
        lazy.layout.increase_nmaster(),
        desc="Grow window to the right"
        ),
    Key([mod], "n", lazy.layout.reset(), desc="Reset all window sizes"),
    ## ----- ##
    Key([mod], "f",
        # lazy.window.toggle_fullscreen(),
        lazy.window.toggle_fullscreen(),
        desc="Toggle fullscreen"
        ),
    ## ----- ##
    Key([mod], "m",
        lazy.layout.maximize(),
        desc="Toggle window between minimum and maximum sizes"
        ),
    ## ----- ##
    Key([mod, "shift"], "Tab",
        lazy.layout.rotate(),
        lazy.layout.flip(),
        desc="Switch which side main pane occupies (MonadTall)"
        ),
    ## ----- ##
    Key([mod], "space",
        lazy.screen.toggle_group(),
        desc='Move to the last visited group'
        ),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack"),

    # }}}


    ### LAUNCH PREFERRED PROGRAMS -----{{{
    # Terminal ---
    Key([mod], "Return", lazy.spawn(terminal)),

    # Application menu ---
#   Key([mod], "d", lazy.spawn("/usr/bin/dmenu_run")),
    Key([mod], "d", lazy.run_extension(extension.Dmenu(
            dmenu_command="dmenu_run",
            dmenu_prompt="command",
            font="Hack",
            fontsize=9,
            background="#08052b",
            foreground="#c099ff",
            selected_background="#82aaff",
            selected_foreground="#000",
        ))),
    Key([mod], "r", lazy.spawn("/usr/bin/rofi -modi drun -show drun -config ~/.config/rofi/moonlight_menu.rasi")),

    # For open applications ---
    KeyChord([mod], "g", [
        Key([], "g", lazy.spawn("gimp")),
        Key([], "i", lazy.spawn("inkscape")),
        Key([], "b", lazy.spawn("blender")),
        ]
    ),

    KeyChord([mod], "p", [
        Key([], "e", lazy.spawn("emacs")),
        Key([], "c", lazy.spawn("code")),
        ]
    ),

    KeyChord([mod], "a", [
        Key([], "f", lazy.spawn("firefox")),
        Key([], "n", lazy.spawn("nitrogen")),
        Key([], "t", lazy.spawn("thunar")),
        ]
    ),

    # }}}

    ### QTILE -----{{{
    # Commands ---
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config file"),
    Key([mod, "shift"], "r", lazy.restart(), desc="Restart Qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),

    # Lock screen ---
    #Key([mod, "shift"], "c", lazy.spawn("./.config/qtile/qt_blur_lock.sh")),
    Key([mod, "shift"], "c", lazy.spawn("betterlockscreen --lock blur")),
    
    # Toggle between different layouts as defined below ---
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),

    # }}}

    ### OTHER USEFUL KEYS -----{{{
    # Media player controls ---
    Key([], "XF86AudioPlay", lazy.spawn("/usr/bin/playerctl play")),
    Key([], "XF86AudioPause", lazy.spawn("/usr/bin/playerctl pause")),
    Key([], "XF86AudioNext", lazy.spawn("/usr/bin/playerctl next")),
    Key([], "XF86AudioPrev", lazy.spawn("/usr/bin/playerctl previous")),


    # Pulse Audio controls ---
    Key([], "XF86AudioMute", lazy.spawn("/usr/bin/pamixer -t && notify-send \"mute: $(pamixer --get-mute)\"")),
    Key([], "XF86AudioLowerVolume", lazy.spawn("/usr/bin/amixer -D pulse sset Master 5%-")),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("/usr/bin/amixer -D pulse sset Master 5%+")),
    
    # Backlight control ---
    Key([], "XF86MonBrightnessUp", lazy.spawn("/usr/bin/xbacklight +5")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("/usr/bin/xbacklight -5")),

    ## Print screen
    # Save to file
    KeyChord([mod], "Print", [
        Key([], "f", lazy.spawn(f'scrot {home}/Pictures/screenshots/%Y-%m-%d-%T-screenshot.png')),
        Key([], "w", lazy.spawn(f'scrot -u {home}/Pictures/screenshots/%Y-%m-%d-%T-screenshot.png')),
        Key([], "s", lazy.spawn(f'scrot --freeze -s {home}/Pictures/screenshots/%Y-%m-%d-%T-screenshot.png')),
        ]
    ),

    # Save to clipboard
    KeyChord(["control"], "Print", [
        Key([], "f", lazy.spawn(f"scrot '/tmp/%F_%T_$wx$h.png' -e 'xclip -selection clipboard -t image/png -i $f'")),
        Key([], "w", lazy.spawn(f"scrot '/tmp/%F_%T_$wx$h.png' -u -e 'xclip -selection clipboard -t image/png -i $f'")),
        Key([], "s", lazy.spawn(f"scrot '/tmp/%F_%T_$wx$h.png' --freeze -s -e 'xclip -selection clipboard -t image/png -i $f'")),
        ]
    ),

    # }}}
]


### STARTUP APPLICATIONS -----{{{
@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.call([home])

# }}}


### COLORS -----{{{
color_dict = {
    "pink": "#ff79c6",
    "purple": "#bd93f9",
    "blue": "#8be9fd",
    "green": "#50fa7b",
    "yellow": "#f1fa8c",
    "orange": "#ffb86c",
    "lightred": "#ff7f7f",
    "red": "#ff5555",
    "darkblue": "#08052b",
    "doom_one_theme_blue": "#51afef",

    '--moonlight-desaturated-gray': '#7f85a3',
    '--moonlight-dark-blue': '#3e68d7',
    '--moonlight-blue': '#82aaff',
    '--moonlight-sky-blue': '#65bcff',
    '--moonlight-cyan': '#86e1fc',
    '--moonlight-red': '#ff757f',
    '--moonlight-dark-red': '#ff5370',
    '--moonlight-light-red': '#ff98a4',
    '--moonlight-yellow': '#ffc777',
    '--moonlight-orange': '#ff966c',
    '--moonlight-dark-orange': '#fc7b7b',
    '--moonlight-teal': '#4fd6be',
    '--moonlight-green': '#c3e88d',
    '--moonlight-purple': '#c099ff',
    '--moonlight-pink': '#fca7ea',
    '--moonlight-indigo': '#7a88cf',
    '--moonlight-bright-cyan': '#b4f9f8',

    '--moonlight-gray-10-alt': '#bcc4d6',
    '--moonlight-gray-10': '#c8d3f5',
    '--moonlight-gray-9': '#b4c2f0',
    '--moonlight-gray-8': '#a9b8e8',
    '--moonlight-gray-7': '#828bb8',
    '--moonlight-gray-6': '#444a73',
    '--moonlight-gray-5': '#2f334d',
    '--moonlight-gray-4': '#222436',
    '--moonlight-gray-3': '#1e2030',
    '--moonlight-gray-2': '#191a2a',
    '--moonlight-gray-1': '#131421',

    '--night-yellow': '#d7b226',
    '--night-magenta': '#7a177d',
    '--night-pink': '#c513a1',
    '--night-purple': '#471562',
}

### LAYOUTS -----{{{
layouts = [
    # layout.Columns(
    #     margin=4,
    #     border_focus=color_dict["doom_one_theme_blue"],
    #     border_normal=color_dict["purple"],
    #     border_width=2,
    #     border_on_single=True,
    # ),
    layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    layout.MonadTall(
        margin=4,
        border_focus=color_dict["--moonlight-blue"],
        border_normal=color_dict["--moonlight-purple"],
        border_width=2,
        border_on_single=True,
    ),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

# }}}

widget_defaults = dict(
    font='Hack',
    fontsize=10,
    padding=3,
)
extension_defaults = widget_defaults.copy()

# }}}


### BATTERY WIDGET -----{{{
bat = widget.Battery()


def get_battery_label():
    percent = bat._load_battery().update_status()[1] * 100
    if (percent < 20):
        return '', '#ff0000'
    elif (percent < 45):
        return '', color_dict["--moonlight-orange"]
    elif (percent < 70):
        return '', color_dict["--moonlight-yellow"]
    elif (percent < 95):
        return '', color_dict["--moonlight-green"]
    else:
        return '', color_dict["--moonlight-gray-10"]


battery = dict(
    battery_name='BAT0',
    energy_now_file='energy_now',
    energy_full_file='energy_full',
    power_now_file='power_now',
    charge_char='',
    discharge_char='',
    update_interval=30,
    format='» ' + get_battery_label()[0] + ' {percent:2.0%} {char}',
    foreground=get_battery_label()[1],
    low_forgeground='ff0000',
    **widget_defaults,
)

battery_widget = widget.Battery(**battery)

# }}}


### CPU TEMPERATURE WIDGET -----{{{
def get_temp_label():
    temp = float(widget.ThermalSensor().get_temp_sensors()['CPU'][0])
    if (temp < 45):
        return ''
    elif (temp < 55):
        return ''
    elif (temp < 65):
        return ''
    elif (temp < 75):
        return ''
    else:
        return ''

# }}}


### GROUPS -----{{{
group_inits = [(' ',  {'layout': 'monadtall', 'matches': Match(wm_class=["Alacritty"])}),
               ('爵 ', {'layout': 'monadtall', 'matches': Match(wm_class=["firefox", "Vieb"])}),
               (' ',  {'layout': 'monadtall', 'matches': Match(wm_class=["Emacs", "Code", "Typora"])}),
               (' ',  {'layout': 'monadtall', 'matches': Match(wm_class=["Thunar"])}),
               (' ',  {'layout': 'monadtall', 'matches': Match(wm_class=["Blender", "Gimp-2.10", "Gimp", "Inkscape", "Nitrogen"])}),
               (' ',  {'layout': 'monadtall', 'matches': Match(wm_class=["Zathura", "Com.github.johnfactotum.Foliate"])}),
               (' ',  {'layout': 'monadtall', 'matches': Match(wm_class=["Io.github.celluloid_player.Celluloid", "mpv"])}),
               (' ',  {'layout': 'monadtall', 'matches': Match(wm_class=["VirtualBox Manager"])}),
               (' ',  {'layout': 'monadtall', 'matches': Match(wm_class=["Thunderbird", "VirtualBox Machine"])})]

groups = [Group(name, **kwargs) for name, kwargs in group_inits]
for i, (name, kwargs) in enumerate(group_inits, 1):
    keys.append(Key([mod], str(i), lazy.group[name].toscreen()))        # Switch to another group
    keys.append(Key([mod, "shift"], str(i), lazy.window.togroup(name))) # Send current window to another group

# }}}


### WIDGETS ON TOP BAR -----{{{
screens = [
    Screen(
        top=bar.Bar(
            [
                widget.Image(
                    filename="~/Pictures/endeavour.png",
                    margin_x=4,
                    margin_y=2,
                ),
                widget.CurrentLayout(
                    foreground=color_dict["--moonlight-red"],
                    fmt='« {} ',
                ),
                widget.GroupBox(
                    active=color_dict["pink"],
                    block_highlight_text_color=color_dict["blue"],
                    borderwidth=2,
                    disable_drag=True,
                    font="RobotoMono Nerd Font",
                    fontsize=10,
                    foreground=color_dict["green"],
                    highlight_color=color_dict["darkblue"],
                    highlight_method='line',
                    inactive=color_dict["--moonlight-purple"],
                    rounded=False,
                    this_current_screen_border=color_dict["blue"],
                ),
#               widget.Prompt(),
                widget.WindowName(
                    foreground="ff0000.00",
                ),
                widget.DF(
                    foreground=color_dict["--moonlight-pink"],
                    format='  {uf}{m}',
                    partition='/home',
                    update_interval=30,
                    visible_on_warn=False,
                ),
                widget.CPU(
                    foreground=color_dict["--moonlight-purple"],
                    format='»  {load_percent}%',
                ),
                widget.Memory(
                    foreground=color_dict["--moonlight-cyan"],
                    format='»  {MemPercent}%',
                    measure_mem='G',
                ),
                widget.ThermalSensor(
                    foreground=color_dict["--moonlight-teal"],
                    fmt='» ' + get_temp_label() + ' {}',
                    tag_sensor='CPU',
                ),
                battery_widget,
                widget.PulseVolume(
                    foreground=color_dict["--moonlight-orange"],
                    fmt='»  {}',
                ),
                widget.Clock(
                    foreground=color_dict["--moonlight-red"],
                    format='» %a, %b %d %I:%M %p »',
                ),
                widget.Systray(),
            ],
            20,
            background="ff0000.00",
#            opacity=0.96,
#            margin=0,
        ),
    ),
]

# }}}


### DRAG FLOATING LAYOUTS -----{{{
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client ---
    *layout.Floating.default_float_rules,
    Match(wm_class='Blueberry.py'),
    Match(wm_class='Bluetooth-sendto'),
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='Galculator'),  # GUI calculator
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='Pamac-manager'),
    Match(wm_class='Pavucontrol'),
    Match(wm_class='qt5ct'),
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(wm_class='Sxiv'),
    Match(wm_class='yad'),  # after install
    Match(wm_class='Xsane'),
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
],
border_focus=color_dict["--moonlight-blue"],
border_normal=color_dict["purple"],
border_width=2,
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not? ---
auto_minimize = True

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
