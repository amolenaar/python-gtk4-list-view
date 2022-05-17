# GTK4 ListView examples

[`Gtk.ListView`](https://docs.gtk.org/gtk4/section-list-widget.html) is the new list and tree widget for GTK4.

I started with a simple list model ([simple_list.py](gtk4_list_view/simple_list.py)).
The next step is to add some hierarchy, make it a tree ([simple_tree.py](gtk4_list_view/simple_tree.py)).

Note that, in the _.ui_ files, `type="__main__+Demo"`. This is because the Demo class is defined in the module
we start (`__main__`).


#Set up

```
poetry install
```

To enable the Python virtual environment:

```
poetry shell
```

To run an example:

```
python -m gtk4_list_view.simple_list
```