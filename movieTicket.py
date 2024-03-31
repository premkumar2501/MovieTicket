class movie:
    def __init__(self,a,b,c,d,e,f):
        self.a=a
        self.b=b
        self.c=c
        self.d=d
        self.e=e
        self.f=f
    def display(self):
        print(f"{self.a},{self.b},{self.c},{self.d},{self.e},{self.f}")
class movie_list(movie):
    def __init__(self):
        super().__init__('Jai bhem','Maanadu','Leo','Vikram','Ayalan','Asuran')
        self.movies={}
    def timing(self):
        time1='6.30 am'
        time2='10.00 am'
        time3='12.45 pm'
        time4='3.00pm'
        time5='5.30 pm'
        time6='8,30pm'
        self.movies.update({f"{self.a}":{'Time':time1,'Ticket prize':120,'Available tic':23},f"{self.b}":{'Time':time2,'Ticket prize':120,'Available tic':15},
                            f"{self.c}":{'Time':time3,'Ticket prize':110,'Available tic':22},f"{self.d}":{'Time':time4,'Ticket prize':130,'Available tic':19},
                            f"{self.e}":{'Time':time5,'Ticket prize':120,'Available tic':17},f"{self.f}":{'Time':time6,'Ticket prize':120,'Available tic':20}})

        
    def booking(self,m_name):
        i_value=self.movies.get(f"{m_name}")
        i_value1=i_value.items()
        for i in i_value1:
            print(i)
        book=int(input('How many ticket get:'))
        tic=self.movies[f"{m_name}"]
        if tic.get('Available tic')>=book:
            total_amount=self.movies[f"{m_name}"]['Ticket prize'] * book
            print('Total amount for tickets:',total_amount)
            print('Your tickets are booked. Enjoy the movie.')
            self.movies[f"{m_name}"]['Available tic']-=book
        else:
            print('House full.')
print('Welcome to PSS Multiplex')
running_movie=movie_list()
running_movie.timing()
print('Select the option: 1.See movie , 2.Book the ticket')
while True:
    choice=input('Enter the choice:')
    if choice=='1':
        running_movie.display()
    else:
        movie_name=input('Which movie:')
        running_movie.booking(movie_name)






        
