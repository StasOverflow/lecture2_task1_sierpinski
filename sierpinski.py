import turtle


def triangle_rotate(vertex_list):
    vertex_list.insert(0, vertex_list.pop())
    return vertex_list


def triangle_draw(carriage, vertex_list):
    carriage.up()
    carriage.setpos(vertex_list[0])
    carriage.down()
    carriage.setpos(vertex_list[1])
    carriage.setpos(vertex_list[2])
    carriage.setpos(vertex_list[0])


def center_get(vertex_first, vertex_second):
    x_coordinate = (vertex_second[0] + vertex_first[0])/2
    y_coordinate = (vertex_second[1] + vertex_first[1])/2
    center = [x_coordinate, y_coordinate]
    return center


def sierpinski_triangle_vertex_list_get(vertex_list):
    sierpinski_vertex_list = list()
    sierpinski_vertex_list.append(vertex_list[0])
    sierpinski_vertex_list.append(center_get(vertex_list[0], vertex_list[1]))
    sierpinski_vertex_list.append(center_get(vertex_list[0], vertex_list[2]))
    return sierpinski_vertex_list


def sierpinski_triangle_draw(carriage, vertex_list, depth):
    if depth:
        triangle_draw(carriage, vertex_list)
        array = vertex_list
        for x in range(len(vertex_list)):
            sub_triangle_vertex_list = sierpinski_triangle_vertex_list_get(vertex_list)
            sierpinski_triangle_draw(carriage, sub_triangle_vertex_list, depth - 1)
            array = triangle_rotate(array)


def main():
    display_window = turtle.Screen()
    my_turtle = turtle.Turtle()
    sierpinski_triangle_draw(my_turtle, [[-50, 0], [50, 0], [0, 86]], 4)
    display_window.exitonclick()


if __name__ == '__main__':
    main()
