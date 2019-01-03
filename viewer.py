import urwid
import monad

def main():
    text_header = ('This is the header')
    divider = urwid.Divider()
    listbox_content = []
    mons = monad.load_monads()
    for mon in mons:
        listbox_content.append(divider)
        listbox_content.append(urwid.Padding(urwid.Text(mon.title),left=2,right=2,min_width=20))

    header = urwid.AttrWrap(urwid.Text(text_header),'header')
    listbox = urwid.ListBox(urwid.SimpleListWalker(listbox_content))
    frame = urwid.Frame(urwid.AttrMap(listbox,'body'),header=header)

    palette=[
        ('header','white','dark red','bold'),
        ('body','black','light gray','black')
    ]
    def unhandled(key):
        if key == 'f8':
            raise urwid.ExitMainLoop()

    urwid.MainLoop(frame,palette,unhandled_input=unhandled).run()

if '__main__' == __name__:

    main()


