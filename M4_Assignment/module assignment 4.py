"""
Design a book class with title, author, publisher, price, and authors Royalty
as instance variables. Provide getter and setter properties for all variables. Also,
define a method Royalty() to calculate Royalty amount author can expect to receive
the following Royaltyties:10%  of the retail price on the first 500 copies; 12.5% for
the next 1,000 copies sold, then 15% for all further copies sold. 
Then design a new ebook class inherited from the book class. Add ebook format
(EPUB, PDF,  MOBI, etc) as an additional instance variable in the inherited class.                                                                                                                                    Override Royalty() method to deduct GST @12% on ebooks.
"""


class book:
    def __init__(self,a='Think Python',b='Allen B. Downey',c=" O'Reilly ",d=525,q=800 ):
        self.title=a
        self.author=b
        self.publisher=c
        self.price=d
        self.copiesSold=q
        Royalty=0
    def get_title(self):
        return self._title
    def set_title(self,a):
        self.title=a
        return
    def get_author(self):
        return self.author
    def set_author(self,b):
        self.author=b
        return
    def get_publisher(self):
        return self.publisher()
    def set_publisher(self,c):
        self.publisher=c
        return
    def get_price(self):
        return self.price
    def set_price(self,d):
        self.price=d
        return
    def get_copiesSold(self):
        return self.copiesSold
    def set_copiesSold(self,e):
        self.copiesSold=e
        return
    def Royalty(self):
        if self.copiesSold<=500:
            Royalty=.1*self.price*self.copiesSold
        elif self.copiesSold>500 and self.copiesSold<=1500:
            Royalty=.125*self.price*(self.copiesSold-500)+.1*self.price*500
        elif self.copiesSold>1500:
            Royalty=.1*self.price*500+.125*self.price*1000+.15*self.price*(self.copiesSold-1500)
        return Royalty

class ebook(book):
    def __init(self,aa='EPUB'):
        self._format=aa
    def get_format(self):
        return self.format
    def set_format(self,b):
        self.format=b
        return
    def Royalty(self):
        if self.copiesSold<=500:
            Royalty=.1*self.price*self.copiesSold
        elif self.copiesSold>500 and self.copiesSold<=1500:
            Royalty=.125*self.price*(self.copiesSold-500)+.1*self.price*500
        elif self.copiesSold>1000:
            Royalty=.1*self.price*500+.125*self.price*1000+.15*self.price*(self.copiesSold-1500)
        Royalty=Royalty-(.12*Royalty)
        return Royalty
a=input(" Enter the title of the book ")
b=input(" Enter the author ofthe book ")
c=input(" Enter the publisher of book ")
d=int(input(" Enter the price of the book "))
e=int(input(" Enter the total number of books sold "))
f=int(input(" Enter 1 for normal book and enter 2 for e book "))
x=book()
x.set_title(a)
x.set_author(b)
x.set_publisher(c)
x.set_price(d)
x.set_copiesSold(e)
y=ebook()
if f==1:
    z=x.Royalty()
    print(" Title is {} \n Publisher is {} \n Author is {} \n Price was {} \n Total sold {} \n Royalty is {} \n".format(x.title,x.publisher,x.author,x.price,x.copiesSold,z))

if f==2:
    g=input("Enter the format of ebook")
    z=y.Royalty()
    y.set_format(g)
    print(" Title is {} \n Publisher is {} \n Author is {} \n Price was {} \n Total sold {} \n Format is {} \n Royalty is {} \n".format(y.title,y.publisher,y.author,y.price,y.copiesSold,y.format,z))
