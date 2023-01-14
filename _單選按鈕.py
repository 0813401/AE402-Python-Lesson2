''' import module '''
import tkinter as tk

''' tkinter GUI '''
window = tk.Tk()
window.title('花生粉的單選按鈕')
window.geometry('500x500')


''' 創建 tk.string 參數 '''
string = tk.StringVar()

''' 定義按下按鈕後回應的function '''
def selection():
    label.config(text = "我喜歡" + string.get())

'''  label '''
label = tk.Label(window, bg = '#f00', text = '尚未選擇')
label.pack()

''' radiobutton1 '''
radio1 = tk.Radiobutton(window, 
                        text = 'Python',
                        variable = string,
                        value = 'Python',
                        command = selection)
radio1.pack()


''' radiobutton2 '''
radio2 = tk.Radiobutton(window, 
                        text = 'C++',
                        variable = string,
                        value = 'C++',
                        command = selection)
radio2.pack()


''' radiobutton3 '''


''' 包裝 menu 並運行 '''
window.mainloop()


