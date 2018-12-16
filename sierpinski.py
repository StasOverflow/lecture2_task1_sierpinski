import turtle


def triangle_draw(carriage, left_vertex, right_vertex, top_vertex):
    carriage.up()
    carriage.goto(left_vertex)
    carriage.down()
    carriage.goto(right_vertex)
    carriage.goto(top_vertex)
    carriage.goto(left_vertex)


def center_get(vertex_first, vertex_second):
    x_coordinate = (vertex_second[0] + vertex_first[0])/2
    y_coordinate = (vertex_second[1] + vertex_first[1])/2
    center = [x_coordinate, y_coordinate]
    return center


def sierpinski_triangle_draw(carriage, vertex_array, depth):
    if depth:
        left_vertex = vertex_array[0]
        right_vertex = vertex_array[1]
        top_vertex = vertex_array[2]
        triangle_draw(carriage, left_vertex, right_vertex, top_vertex)
        turns = 0
        while turns < 3:
            cell = turns
            left_vertex = vertex_array[cell]
            if cell + 1 >= 3:
                cell = 0
            else:
                cell = cell + 1
            right_vertex = vertex_array[cell]
            if cell + 1 >= 3:
                cell = 0
            else:
                cell = cell + 1
            top_vertex = vertex_array[cell]
            left_sub_vertex = left_vertex
            right_sub_vertex = center_get(left_vertex, right_vertex)
            top_sub_vertex = center_get(left_vertex, top_vertex)
            sub_vertex_array = [left_sub_vertex, right_sub_vertex, top_sub_vertex]
            sierpinski_triangle_draw(carriage, sub_vertex_array, depth - 1)
            turns = turns + 1


def main():
    display_window = turtle.Screen()
    my_turtle = turtle.Turtle()
    sierpinski_triangle_draw(my_turtle, [[-50, 0], [50, 0], [0, 86]], 5)
    display_window.exitonclick()


if __name__ == '__main__':
    main()
