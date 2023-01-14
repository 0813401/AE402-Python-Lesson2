''' import module '''
import tkinter as tk

''' tkinter GUI '''
window = tk.Tk()
window.title('花生粉_Menu')
window.geometry('500x500')

''' menu '''
menuBar = tk.Menu(window)

''' 子 menu1 '''
fileMenu = tk.Menu(menuBar, tearoff = False)
fileMenu.add_command(label = '新增檔案')
fileMenu.add_command(label = '儲存檔案')
fileMenu.add_separator()
fileMenu.add_command(label = '說掰掰')
menuBar.add_cascade(label = '檔案', menu = fileMenu)

''' 子 menu2 '''


''' 子子 menu (隨堂挑戰) '''


''' 包裝 menu 並運行 '''
window.config(menu = menuBar)
window.mainloop()
