
import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class MyWindow(Gtk.Window):
    def __init__(self):

        Gtk.Window.__init__(self, title="SNURSING SYSTEM")
        self.set_border_width(10)
        #self.set_default_size(1920,1080)
        self.notebook = Gtk.Notebook()
        self.add(self.notebook)
#page 1-------------------------------------------------------------------------------
        self.page1 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)

        self.page1.set_border_width(200)
        # senter username
        self.page1.add(Gtk.Label("ID"))
        self.username = Gtk.Entry()

        #senter password
        self.password = Gtk.Entry()
        self.password.set_visibility(False)
        self.page1.add(Gtk.Label("password"))

        #connect button
        self.notebook.append_page(self.page1, Gtk.Label("wifi"))
        self.button=Gtk.Button(label="connect")
        self.button.connect("clicked",self.sign_in)

        self.page1.pack_start(self.username, True, True, 0)
        self.page1.pack_start(self.password, True, True, 0)
        self.page1.pack_start(self.button, True, True, 0)

#page2--------------------------------------------------------------------------------------------------
        self.page2 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.page2.set_border_width(200)
        self.page2.add(Gtk.Label("choose medcine"))
        # medcine combobox
        # medicine =Gtk.ListStore(int, str)
        # medicine.append([11," headache"])
        # medicine.append([12,"Toothache"])
        # medicine.append([2,"Allergy"])
        # medicine.append([3,"Burns"])
        # medicine.append([31, "Indigestion"])
        # combo_med= Gtk.ComboBox.new_with_model_and_entry(medicine)
        # #combo_med.connect("changed", self.on_combo_medicine_changed)
        # combo_med.set_entry_text_column(1)

        medicine = [
            "headache",
            "toothache",
            "allergy",
            "burns",
            "Indigestion",

        ]

        combo_med = Gtk.ComboBoxText()
        combo_med.set_entry_text_column(0)
        for me in medicine:
            combo_med.append_text(me)


        self.button2 = Gtk.Button(label="Give it")
        self.button2.connect("clicked", self.give_medicine,combo_med)

        self.button3 = Gtk.Button(label='add')
        self.button3.connect("clicked", self.add_medicine)

        self.page2.pack_start(combo_med, False, False, 0)
        self.page2.pack_start(self.button2, True, True, 0)
        self.page2.pack_start(self.button3, True, True, 0)
        self.notebook.append_page(self.page2, Gtk.Label("manual dose"))
        # --------------------------------
        # ------------------------------------------------------------

        # self.label = combo_med.get_active()


#page3---------------------------------------------------------------------------------------------------
        self.page3 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.page3.set_border_width(200)
# ------------------------------------------------------------------------------------------
        a =Gtk.ListStore(int, str)
        a.append([11, "Billy Bob Junior"])
        a.append([12, "Sue Bob"])
        a.append([2, "Joey Jojo"])
        a.append([3, "Rob McRoberts"])
        a.append([31, "Xavier McRoberts"])

        combo_caller = Gtk.ComboBox.new_with_model_and_entry(a)

        combo_caller.set_entry_text_column(1)
        self.page3.pack_start(combo_caller, False, False, 0)
        self.notebook.append_page(self.page3, Gtk.Label("conntect care giver"))

 #buttons--------------------------------------------------------------------
        add_button= Gtk.Button.new_with_label("add")
        add_button.connect("clicked", self.on_add_clicked)
        self.page3.pack_start(add_button, True, True, 0)

        remove_button = Gtk.Button(label="remove")
        remove_button.connect("clicked", self.on_remove_clicked)
        self.page3.pack_start(remove_button, True, True, 0)

        call_button = Gtk.Button(label="call")
        call_button.connect("clicked", self.on_call_clicked)
        self.page3.pack_start( call_button, True, True, 0)
#---------------------------------------------------------------------------------------------
        tree_iter2 = combo_caller.get_active_iter()
        if tree_iter2 is not None:
            model = combo_caller.get_model()
            row_id2, name2 = model[tree_iter][:2]

        else:
            entry = combo_caller.get_child()


# page4---------------------------------------------------------------------------------------------------
        self.page4 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.page4.set_border_width(200)
        self.notebook.append_page(self.page4, Gtk.Label("features"))
#------------------------------------------------------------
    def on_combo_medicine_changed(self, combo):
        tree_iter = combo.get_active_iter()
        if tree_iter is not None:
            model = combo.get_model()
            row_id, name = model[tree_iter][:2]

        else:
            entry = combo.get_child()
# connect button for page 1----------------------------------------------------------------------
    def sign_in(self, widget):
        print(self.username.get_text())
        print(self.password.get_text())
#give it and add button for PAGE 2---------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------
    def give_medicine(self, widget,wid):
        text = wid.get_active_text()
        if text is not None:
            print("Selected: currency=%s" % text)

        # if text is not None:
        #     print("Selected: currency=%s" % self.text)




    def add_medicine(self, widget):

        combo.append_text(self.text)
#buttons page 3--------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------
    def on_add_clicked(self, add_button):
        print("Selected: ID=%d, name=%s" % (row_id2, name2))
    def on_remove_clicked(self, remove_button):
         combo_caller.remove_text( row_id2)

    def on_call_clicked(self, call_button):
        print("Selected: ID=%d, name=%s" % (row_id2, name2))

#-------------------------------------------------------------------------------------------------------
win = MyWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
