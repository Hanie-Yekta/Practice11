import arcade
import random

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400

class Enemy(arcade.Sprite):
    #tabe vizhegi ha
    def __init__(self):
        #erth bari vizhegi haye pedar
        super().__init__()
    
        #vizhegi haye khod tabe
        self.color=arcade.color.GREEN
        self.width=10
        self.height=40
        self.speed=3
        self.point=0
        self.center_x=(SCREEN_WIDTH // 2)+280
        self.center_y=SCREEN_HEIGHT // 2
        self.change_y=0

    def move(self):
            self.center_y += self.speed*self.change_y
    
    def score(self):
        #bord
        self.point += 1

    #namayesh dar safheye bazi
    def draw(self):
        #dayereye tu por ba abaad moshakhas shode
        arcade.draw_rectangle_filled(self.center_x,self.center_y,self.width,self.height,self.color)
    
        #chaap score
        arcade.draw_text(f"{self.point}",self.center_x-220,SCREEN_HEIGHT-30)


class Player(arcade.Sprite):
    #tabe vizhegi ha
    def __init__(self):
        #erth bari vizhegi haye pedar
        super().__init__()
    
        #vizhegi haye khod tabe
        self.color=arcade.color.YELLOW
        self.width=10
        self.height=50
        self.change_y=0
        self.speed=2
        self.point=0
        self.center_x=(SCREEN_WIDTH // 2)-280
        self.center_y=SCREEN_HEIGHT // 2
    
    def move(self):
   
        #update kardan mokhtasat dasteye player
        if self.change_y > 0:
            self.center_y += self.speed

        elif self.change_y < 0:
            self.center_y-=self.speed
    
    def score(self):#?????
        #bord
        self.point += 1



    #namayesh dar safheye bazi
    def draw(self):
        #dayereye tu por ba abaad moshakhas shode
        arcade.draw_rectangle_filled(self.center_x,self.center_y,self.width,self.height,self.color)

        #chaap score
        arcade.draw_text(f"{self.point}",self.center_x+210,SCREEN_HEIGHT-30)

class Ball(arcade.Sprite):
    #tabe vizhegi ha
    def __init__(self):
        #erth bari vizhegi haye pedar
        super().__init__()


        #vizhegi haye khod tabe
        self.width=10
        self.height=10
        self.color=arcade.color.RED
        self.r=5
        self.center_x=SCREEN_WIDTH //2
        self.center_y=SCREEN_HEIGHT//2
        self.change_x=random.randint(-2,2)
        self.change_y=random.randint(-2,2)
        self.speed=2


    def move(self):
        self.center_x+=self.speed*self.change_x
        self.center_y+=self.speed*self.change_y
       

    #namayesh dar safheye bazi   
    def draw(self):
        #dayereye tu por ba abaad moshakhas shode
        arcade.draw_circle_filled(self.center_x,self.center_y,self.r,self.color)

class Game(arcade.Window):
    #tabe vizhegi ha
    def __init__(self):
        super().__init__(width=SCREEN_WIDTH,height=SCREEN_HEIGHT,title="Pong Game")
        self.background_color=arcade.color.BLACK

        #sakht shei class Ball
        self.ball=Ball()

        #sakht shei class Player
        self.player=Player()

        #sakht shei class enemy
        self.enemy=Enemy()

        ####?
        self.topHit=0
        self.bottomHit=0



    #namayesh dar safheye bazi 
    def on_draw(self):
        #render giri
        arcade.start_render()

        #namayesh ball dar zman ejraye safheye bazi
        self.ball.draw()

        #namayesh player dar zman ejraye safheye bazi
        self.player.draw()

        #namayesh enemy dar zman ejraye safheye bazi
        self.enemy.draw()
    

    #tamam manteq bazi(etefaqat drun bazi)
    def on_update(self, delta_time: float):
        self.player.move()
        self.enemy.move()
        self.ball.move()


        ##########??????
        #check kardan baekhord ball va player
        if arcade.check_for_collision(self.player,self.ball):
            pass #????????????

        #check kardan baekhord ball va Enemy
        if arcade.check_for_collision(self.enemy,self.ball):
            pass 
        ##########

        #shart bakht
        if self.ball.center_x>self.enemy.center_x+5:
            self.player.point +=1
            self.ball=Ball()
    
        if self.ball.center_x<self.player.center_x-5:
            self.enemy.point +=1
            self.ball=Ball()

        self.ball.move()

        #########################################????
        if self.ball.center_y>SCREEN_HEIGHT:
            self.topHit=1
            self.bottomHit=0
        

        if self.ball.center_y<0:
            self.bottomHit=1
            self.topHit=0 
        ###############################

        #harkart daste enemy
        if(self.ball.center_y<self.enemy.center_y):
            self.enemy.change_y=-1
        elif(self.ball.center_y>self.enemy.center_y):
            self.enemy.change_y=+1
        elif(self.ball.center_y==self.enemy.center_y):
            self.enemy.center_y=self.ball.center_y

    
            

    #pas az bardashtan angosht az roy dokme ejra mishavad
    def on_key_release(self, key: int, modifiers: int):

        #taein dokme va noe taqiraat harkat daste
        if key==arcade.key.UP:
            self.player.change_y = 1

        elif key==arcade.key.DOWN:
            self.player.change_y = -1



#####################################

Sgame=Game()

#baraye baste nashodan barname
arcade.run()