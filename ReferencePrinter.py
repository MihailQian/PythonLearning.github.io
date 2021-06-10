'''參考文獻格式生成器'''
# def Reference_essay(
#    Name, Title, Journal, Year, Vol, Page_st, Page_ed):
def Reference_Essay():
    Name = input("论文作者姓名:")
    Title = input("文章標題：")
    Journal = input("期刊名：")
    Year = input("期刊年份：")
    Vol = input("期數：")
    Page_st = input("起始頁碼：")
    Page_ed = input("終止頁碼（如只有一頁請忽略此項）：")
    while int(Page_st)  > int(Page_ed):
        Page_st=input("起始页码或输入错误，请重新输入：")
        Page_ed=input("终止页码或输入错误，请重新输入：")
    if  Page_ed==True and int(Page_ed)==int(Page_st):
        print(f"{Name}.{Title}[J].{Journal},{Year},{Vol}:{Page_st}-{Page_ed}")
    else:
        print(f"{Name}.{Title}[J].{Journal},{Year},{Vol}:{Page_st}")


def Reference_Book():
    Author = input("图书作者姓名：")
    BookTitle = input("书名:")
    Publisher = input("出版社：")
    Area = input("出版地區：")
    PubYear = input("出版年份：")
    Page_st = input("起始頁碼：")
    Page_ed = input("終止頁碼（如只有一頁請忽略此項）：")
    while int(Page_st)  > int(Page_ed):
        Page_st=input("起始页码或输入错误，请重新输入：")
        Page_ed=input("终止页码或输入错误，请重新输入：")

    if Page_ed==True and int(Page_ed)==int(Page_st):
        print(f"{Author}.{BookTitle}[M].{Publisher}:{Area},{PubYear}:{Page_st}-{Page_ed}")
    else:
        print(f"{Author}.{BookTitle}[M].{Publisher}:{Area},{PubYear}:{Page_st}")

"""請在函數Reference_Printer()中輸入“图书”或“期刊”。"""
def Reference_Printer(Type):

    if Type == "期刊":
        Reference_Essay()
    if Type == "图书":
        Reference_Book()
    if Type!="期刊" and Type != "图书":
        print("抱歉，目前仅支持「图书」和「期刊」名类。")

Reference_Printer("书籍")
Reference_Printer("图书")
Reference_Printer("期刊")
















