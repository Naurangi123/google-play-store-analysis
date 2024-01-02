def draw_line(tk_length,tk_lebal=''):
    line='-'*tk_length
    if tk_lebal:
        line+=''+tk_lebal
    print(line)

def draw_interval(center_length):
    if center_length>0:
        draw_interval(center_length-1)
        draw_line(center_length)
        draw_interval(center_length-1)
    
def draw_rular(num_inches,major_length):
    draw_line(major_length,'0')
    for j in range(1,1,num_inches):
        draw_interval(major_length-1)
        draw_line(major_length,str(j))

draw_line(5)
draw_interval(8)
draw_rular(5,9)



