from typing import List  # noqa: F401

import os
import subprocess
from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile import qtile

mod = "mod4" # Super Key
terminal = "alacritty" # My terminal

keys = [
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(),
        desc="Move window focus to other window"),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(),
        desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(),
        desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(),
        desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),

    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(),
        desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(),
        desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(),
        desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack"),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "x", lazy.window.kill(), desc="Kill focused window"),

    Key([mod, "control"], "r", lazy.restart(), desc="Restart Qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "d", lazy.spawn("dmenu_run"),
        desc="Spawn a command using a prompt widget"),
]

group_names = [
    ("",{'layout': 'monadtall'}),
    ("",{'layout': 'monadtall'}),
    ("",{'layout': 'monadtall'}),
    ("",{'layout': 'floating'}),
    ("",{'layout': 'floating'}),
    ("",{'layout': 'floating'}),
    ("",{'layout': 'monadtall'}),
    ("",{'layout': 'monadtall'}),
    ("",{'layout': 'floating'}),
]

colors = [
    "030403", # BG
    "ffffff", # FG
    "4d5562", # P1
    "383c44",# P2
]
groups = [Group(name, **kwargs) for name, kwargs in group_names]

for i, (name, kwargs) in enumerate(group_names, 1):
    keys.append(Key([mod], str(i), lazy.group[name].toscreen()))        # Switch to another group
    keys.append(Key([mod, "shift"], str(i), lazy.window.togroup(name))) # Send current window to another group

layout_defaults = {
    "border_width": 2,
    "margin": 8,
    "border_focus": colors[3],
    "border_normal": "1D2330"
}



layouts = [
    layout.Columns(**layout_defaults),
    layout.Max(**layout_defaults),
    # Try more layouts by unleashing below layouts.
    layout.Stack(num_stacks=2,**layout_defaults),
    layout.Bsp(**layout_defaults),
    layout.Matrix(**layout_defaults),
    layout.MonadTall(**layout_defaults),
    layout.MonadWide(**layout_defaults),
    layout.RatioTile(**layout_defaults),
    layout.Tile(**layout_defaults),
    layout.TreeTab(**layout_defaults),
    layout.VerticalTile(**layout_defaults),
    layout.Zoomy(**layout_defaults),
    layout.Floating(border_width=0, border_focus=colors[1]),
]



widget_defaults = dict(
    font='Ubuntu',
    fontsize=12,
    foreground= colors[1],
    background=colors[0],
    padding=2,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
          [
                widget.GroupBox(
                    font="Ubuntu Mono",
                    highlight_color= colors[2],
                    rounded=False,
                    border_width=0,
                    highlight_method="block",
                    active=colors[1],
                    urgent_text="ffffff",
                    inactive="fcfcfc",
                    background=colors[0],
                    padding=5,
                    margin_y = 3.7,
                ),
                widget.Sep(
                       foreground=colors[0],
                       background=colors[0],
                       padding = 5,
                ),
                widget.WindowName(
                   font="Ubuntu Medium",
                   format="{name}",
                   max_chars=30,
                    
                ),
                
                ###########################
                ###### RIGHT WIDGETS ######
                ###########################

                # Enable notifications if you want by uncommenting code beneath
                widget.Notify(),
                widget.TextBox(
                    text="",
                    foreground=colors[2],
                    background=colors[0],
                    
                    fontsize=53,
                    padding=-0.1
                ),             

                widget.Systray(
                    background=colors[2],
                    paddding=9
                ),

                widget.TextBox(
                    text="",
                    foreground=colors[3],
                    background=colors[2],
                    
                    fontsize=53,
                    padding=-0.1

                ),
                widget.TextBox(
                    text="",
                    background=colors[3],
                ),
                widget.OpenWeather(
                    format="{main_temp} °{units_temperature}",
                    cityid="1266049",
                    background=colors[3]
                ),

                widget.TextBox(
                    text="",
                    foreground=colors[2],
                    background=colors[3],
                    
                    fontsize=53,
                    padding=-0.1
                ),
                widget.Net(
                    format="{down} ↓↑ {up}",
                    background=colors[2]
                ),          
                widget.TextBox(
                    text="",
                    foreground=colors[3],
                    background=colors[2],
                    fontsize=53,
                    padding=-0.1
                ),
                      
                widget.TextBox(
                    text="",
                    background=colors[3],
                    padding=0
                ),
                widget.CPU(
                    format='{freq_current}GHz', # Append this, if you want to show percentage `{load_percent}%`
                    background=colors[3],
                    padding=3
                ),
                widget.TextBox(
                    text="",
                    foreground=colors[2],
                    background=colors[3],
                    fontsize=38,
                    padding= -0.1
                ),
                widget.CurrentLayoutIcon(
                       custom_icon_paths = [os.path.expanduser("~/.config/qtile/icons")],
                       foreground = colors[0],
                       background = colors[2],
                       padding = 3,
                       scale = 0.7
                ),
                widget.TextBox(
                    text="",
                    foreground=colors[3],
                    background=colors[2],
                    fontsize=38,
                    padding=-0.1
                ),
                widget.TextBox(
                    text="",
                    background=colors[3],
                    padding=0
                ),
                widget.Memory(background=colors[3]),
                widget.TextBox(
                    text="",
                    foreground=colors[2],
                    background=colors[3],
                    fontsize=38,
                    padding=-0.1
                ),

                widget.CheckUpdates(
                       update_interval = 1800,
                       distro = "Arch",
                       display_format = " {updates}",
                       foreground = colors[2],
                       background= colors[2],
                       mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(terminal + ' -e sudo pacman -Syu')},
                ),
                widget.TextBox(
                    text="",
                    foreground=colors[3],
                    background=colors[2],
                    
                    fontsize=53,
                    padding=-0.1
                ),
                widget.TextBox(
                    text="",
                    background=colors[3]
                ),
                widget.Volume(
                    format="{volume}",
                    background=colors[3]
                ),
                widget.TextBox(
                    text="",
                    foreground=colors[2],
                    background=colors[3],
                    
                    fontsize=53,
                    padding=-0.1
                ),

                widget.Clock(
                    format=' %a %d, %I:%M',
                    background=colors[2]
                ),

            ],
            26,
            background=colors[1],
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None  # WARNING: this is deprecated and will be removed soon
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
])
auto_fullscreen = True
focus_on_window_activation = "smart"

@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser('~')
    subprocess.call([home + '/.config/qtile/autostart.sh'])

# start_once()
# def autostart():
  #  processes = [
   #     ['/usr/bin/setxkbmap', '-option', 'caps:swapescape'],
    #    ['feh', '--bg-scale', '/home/user/Pictures/wallpaper/archfoil.jpg'],
     #   ['blueman-applet'],
      #  ['nextcloud']
    #]

    #for p in processes:
     #   subprocess.Popen(p)

wmname = "LG3D"
