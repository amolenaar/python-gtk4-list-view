import importlib.resources

from gi.repository import Gio, GLib, GObject, Gtk


def new_list_item_ui():
    with importlib.resources.path("gtk4_list_view", "simple_tree.ui") as ui_path:
        return GLib.Bytes.new(ui_path.read_bytes())


class Demo(GObject.GObject):
    def __init__(self, name):
        super().__init__()
        self._name = name

    @GObject.Property(type=str)
    def name(self):
        return self._name


if __name__ == "__main__":

    model = Gio.ListStore.new(Demo)
    model.append(Demo("one"))
    model.append(Demo("two"))
    model.append(Demo("three"))

    app = Gtk.Application.new("gtk4.listview.SimpleTree", 0)

    def activate(app):
        w = Gtk.Window()
        w.set_title("Simple tree")
        w.set_default_size(400, 400)
        app.add_window(w)

        def child_model(item, user_data):
            return model

        # Our data objects are wrapped by a Gtk.TreeListRow
        tree = Gtk.TreeListModel.new(
            model,
            passthrough=False,
            autoexpand=False,
            create_func=child_model,
            user_data=None,
        )

        selection = Gtk.SingleSelection.new(tree)
        factory = Gtk.BuilderListItemFactory.new_from_bytes(None, new_list_item_ui())

        lv = Gtk.ListView.new(selection, factory)
        w.set_child(lv)
        w.show()

    app.connect("activate", activate)
    app.run()
