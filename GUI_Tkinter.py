
import tkinter
from tkinter import ttk
from tkinter import Menu

# 创建一个窗口对象
win = tkinter.Tk()
# 设置标题
win.title("自动化测试系统")
# 设置窗口大小和位置
win.geometry("960x800+500+50")

"""*****************************************************************************************************************"""
"""进入消息循环 """


def showinfo():
    print(entry.get())


# 创建标签控件
# wraplength 设置文本多宽才换行
label = tkinter.Label(win,
                      text="自动化测试管理系统",
                      bg="pink",
                      fg="blue",
                      font=("黑体", 20),
                      width=18,
                      height=1,
                      justify="left",   # 设置文本换行后的对齐方式
                      anchor="center")  # 设置文本位置(n/e/s/w/center)
# 将标签控件显示出来
label.place(x=320, y=10)
# label.pack()
# 设置焦点,绑定小控件响应按键时才需要对对小控件设置焦点,如果是win窗体则无需设置焦点也能响应按键
label.focus_set()


def func1(event):
    print("event.char=", event.char)
    print("event.key_code=", event.keycode)


label.bind('<Key>', func1)      # Key可以响应所有的键盘按键
"""*****************************************************************************************************************"""
# 创建按钮控件
show_button = tkinter.Button(win,
                             text="获取Text控件文本",
                             command=showinfo,
                             bg="light green",
                             fg="blue",
                             font=("黑体", 20),
                             width=16,
                             height=1,
                             anchor="center")
# show_button.pack()
show_button.place(x=10, y=80)

button2 = tkinter.Button(win,
                         text="执行匿名函数",
                         command=lambda: print("执行了一个匿名函数!"),
                         bg="light green",
                         fg="blue",
                         font=("黑体", 20),
                         width=16,
                         height=1,
                         anchor="center")
# button2.pack()
button2.place(x=10, y=180)

exit_button = tkinter.Button(win,
                             text="退出界面",
                             command=win.quit,
                             bg="light green",
                             fg="blue",
                             font=("黑体", 20),
                             width=16,
                             height=1,
                             anchor="center")
# exit_button.pack()
exit_button.place(x=10, y=280)
"""*****************************************************************************************************************"""
# 创建输入控件,用于显示简单的文本内容
e = tkinter.Variable()                                           # 绑定变量
entry = tkinter.Entry(win, font=("黑体", 30), textvariable=e)     # e就代表了输入框这个对象
e.set("请输入文本文字...")                                          # 设置值
print(e.get())                                                   # 取出输入框里面的值
# entry.pack()
entry.place(x=10, y=380)
"""*****************************************************************************************************************"""
# 创建Listbox控件
# 绑定变量
lbv = tkinter.StringVar()
# lb = tkinter.Listbox(win, selectmode=tkinter.SINGLE, listvariable=lbv)    # 与BROWSE相似,但是不支持鼠标被按下时移动选中位置
lb = tkinter.Listbox(win, selectmode=tkinter.EXTENDED, listvariable=lbv)    # EXTENDED让Listbox控件支持SHIFT和CRTL实现多选
# lb = tkinter.Listbox(win, selectmode=tkinter.BROWSE, listvariable=lbv)
# lb.pack()
# lb.place(x=320, y=100)

# 为列表控件创建滚动条
sc = tkinter.Scrollbar(win)
sc.pack(side=tkinter.RIGHT, fill=tkinter.Y)
lb.configure(yscrollcommand=sc.set)
lb.pack(side=tkinter.RIGHT, fill=tkinter.BOTH)
sc['command'] = lb.yview()

for item in ['one', 'two', 'three', 'four', 'five', 'one1', 'two1', 'three1', 'four1', 'five1',
             'one2', 'two2', 'three2', 'four2', 'five2', 'one3', 'two3', 'three3', 'four3', 'five3']:
    lb.insert(tkinter.END, item)
lb.insert(tkinter.ACTIVE, 'ten')
# lb.delete(1, 4)                   # 删除
lb.select_set(1, 4)                 # 选中
# lb.select_clear(1, 4)             # 取消选中
print(lb.size())                    # 获取列表控件中元素的个数
print(lb.get(2))                    # 从列表控件中取值
print(lb.curselection())            # 返回当前的索引项(元素的下标),注意:不是item
print(lb.selection_includes(0))     # 判断一个选项是否被选中
print(lbv.get())                    # 打印当前列表中选项
# lbv.set(('1', '2', '3'))          # 设置选项


def action(event):
    print(lb.get(lb.curselection()))


lb.bind('<Double-Button-1>', action)  # 绑定事件(双击鼠标左键)
"""*****************************************************************************************************************"""
# 创建Scale控件
scale1 = tkinter.Scale(win, from_=0, to=150, length=400, tickinterval=20, orient=tkinter.HORIZONTAL)
scale1.place(x=320, y=100)
# 设置值
# scale1.set(20)


def show_num():              # 取值
    print(scale1.get())


# tkinter.Button(win, text='Scale取值', comm=show_num).pack()
tkinter.Button(win, text='Scale取值', comm=show_num).place(x=320, y=180)
"""*****************************************************************************************************************"""
# 创建数组范围Spinbox控件


def up_data():
    print(spv.get())


# 绑定一个变量
spv = tkinter.StringVar()
# 参数increment 是步长,默认值为1
# 参数values() 是元组,不要跟参数from_/to/increment同时使用
sp = tkinter.Spinbox(win, from_=0, to=50, increment=5, textvariable=spv, command=up_data)
# 设置值
spv.set(5)
# 取值
print(spv.get())
sp.place(x=320, y=220)
"""*****************************************************************************************************************"""
# 创建顶层菜单
menubar = tkinter.Menu(win)     # 创建菜单条
win.config(menu=menubar)        # 配置菜单
# 创建菜单选项
menu1 = tkinter.Menu(menubar, tearoff=False)
# 给菜单选项条件内容
for item in ['Python', 'C', 'C++', 'C#', 'Java', 'JS', 'Labview', 'Css', '汇编', 'OC', 'Shell','PHP', 'NodeJS', '退出']:
    if item == '退出':
        menu1.add_separator()   # 添加分割线
        menu1.add_command(label=item, command=win.quit)
    else:
        menu1.add_command(label=item)
# 向菜单条上添加菜单选项
menubar.add_cascade(label="语言", menu=menu1)
"""*****************************************************************************************************************"""
# 右击鼠标显示菜单
"""menubar1: Menu = tkinter.Menu(win)
menu2 = tkinter.Menu(menubar)
for item in ['Python', 'C', 'C++', 'C#', 'Java', 'JS', 'Labview', 'Css', '汇编', 'OC', 'Shell','PHP', 'NodeJS', '退出']:
    menu2.add_command(label=item)
menubar1.add_cascade(label="语言", menu=menu2)"""


def show_menu(event):
    menubar.post(event.x_root, event.y_root)


win.bind('<Button-3>', show_menu)
"""*****************************************************************************************************************"""
# 创建Combobox下拉控件
combo = ttk.Combobox(win)
combo.place(x=320, y=250)
# 设置下拉数据
combo["value"]=("广州", "佛山", "东莞", "深圳")
# 设置默认值
combo.current(1)
# 绑定事件


def func(event):
    print(combo.get())


combo.bind("<<ComboboxSelected>>", func)
"""*****************************************************************************************************************"""
# 创建Frame框架控件,在屏幕上显示一个矩形区域,当做容器使用
frm = tkinter.Frame(win)
# frm.pack()
frm.place(x=320, y=300)
# 左侧布局Frame
frm_l = tkinter.Frame(frm)
tkinter.Label(frm_l, text="左上", bg="pink").pack(side=tkinter.TOP)
tkinter.Label(frm_l, text="左下", bg="blue").pack(side=tkinter.TOP)
frm_l.pack(side=tkinter.LEFT)
# 右侧布局Frame
frm_r = tkinter.Frame(frm)
tkinter.Label(frm_r, text="右上", bg="red").pack(side=tkinter.TOP)
tkinter.Label(frm_r, text="右下", bg="green").pack(side=tkinter.TOP)
frm_r.pack(side=tkinter.RIGHT)
"""*****************************************************************************************************************"""
# 创建表格数据
table = ttk.Treeview(win)
table.place(x=50, y=500)
# 定义列
table["columns"] = ("测试值1", "测试值2", "测试值3", "测试值4", "测试值5")
# 设置列,列还不显示
table.column("测试值1", width=90)
table.column("测试值2", width=90)
table.column("测试值3", width=90)
table.column("测试值4", width=90)
table.column("测试值5", width=90)

# 设置表头
table.heading("测试值1", text="测试值a")
table.heading("测试值2", text="测试值b")
table.heading("测试值3", text="测试值c")
table.heading("测试值4", text="测试值d")
table.heading("测试值5", text="测试值e")

# 添加数据
table.insert("", 0, text="工位一", values=("100", "200", "300", "400", "500"))
table.insert("", 1, text="工位二", values=("600", "700", "800", "900", "1000"))
table.insert("", 2, text="工位三", values=("1100", "1200", "1300", "1400", "1500"))
"""*****************************************************************************************************************"""
# 创建树状数据
tree = ttk.Treeview(win)
tree.place(x=550, y=200)
# 添加一级树枝
treeF1 = tree.insert("", 0, "工程部", text="工程部1", values="F1")
treeF2 = tree.insert("", 1, "人力资源部", text="人力资源部1", values="F2")
treeF3 = tree.insert("", 2, "制造部", text="制造部1", values="F3")
# 添加二级树枝
treeF1_1 = tree.insert(treeF1, 0, "小组1", text="小组1", values="F1_1")
treeF1_2 = tree.insert(treeF1, 1, "小组2", text="小组2", values="F1_2")
treeF1_3 = tree.insert(treeF1, 2, "小组3", text="小组3", values="F1_3")

treeF2_1 = tree.insert(treeF2, 0, "小组11", text="小组1", values="F2_1")
treeF2_2 = tree.insert(treeF2, 1, "小组21", text="小组2", values="F2_2")
treeF2_3 = tree.insert(treeF2, 2, "小组31", text="小组3", values="F2_3")

treeF3_1 = tree.insert(treeF3, 0, "小组12", text="小组1", values="F3_1")
treeF3_2 = tree.insert(treeF3, 1, "小组22", text="小组2", values="F3_2")
treeF3_3 = tree.insert(treeF3, 2, "小组32", text="小组3", values="F3_3")
# 添加三级树枝
treeF1_1_1 = tree.insert(treeF1_1, 0, "员工1", text="员工1", values="F1_2")
treeF1_1_2 = tree.insert(treeF1_1, 1, "员工2", text="员工2", values="F1_2")
treeF1_1_3 = tree.insert(treeF1_1, 2, "员工3", text="员工3", values="F1_2")
"""*****************************************************************************************************************"""
win.mainloop()







