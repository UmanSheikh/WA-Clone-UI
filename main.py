from kivymd.app import MDApp
from kivymd.uix.tab import MDTabsBase, MDTabs
from kivymd.uix.floatlayout import MDFloatLayout

class Tab(MDFloatLayout, MDTabsBase):
      def on_tab_switch(self, instance_tabs, instance_tab, instance_tab_label, tab_text):
        '''Called when switching tabs.

        :type instance_tabs: <kivymd.uix.tab.MDTabs object>;
        :param instance_tab: <__main__.Tab object>;
        :param instance_tab_label: <kivymd.uix.tab.MDTabsLabel object>;
        :param tab_text: text or name icon of tab;
        '''

        instance_tab.ids.label.text = tab_text


class MainApp(MDApp):
    def on_start(self):
        self.theme_cls.primary_palette = "Gray"
        self.theme_cls.theme_style = "Dark"

    def on_tab_switch(self, instance_tabs, instance_tab, instance_tab_label, tab_text):
        pass
    



if __name__ == '__main__':
    MainApp().run()