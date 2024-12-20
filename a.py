import turtle

def square(t):
    for i in range(4):
        t.forward(100)  
        t.left(90)      

bob = turtle.Turtle()  # タートルを作成
square(bob)            

turtle.done()          # 描画完了後、ウィンドウを閉じずに待機
