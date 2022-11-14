#!/usr/bin/env python3

def visualize_str(tape: list, selected_pos: int = -1, start: int = 0, cells: int = 0) -> str:

    output = ''

    #iterations = lambda: range(start, len(tape[start:start+(cells or len(tape))]) + 1)
    upper = min(start + (cells or len(tape)) + 1, len(tape) + 1)
    iterations = lambda: range(start, upper)

    for i in iterations():
        cell_header = f'{"▼" if i - 1 == selected_pos and i != 0 else "": ^5}'
        output += f'{cell_header} '

    output += ' ' * 5 + '\n'

    for _ in iterations():
        output += '─────┬'

    output += '─────\n'

    for i in iterations():

        center = str(tape[i - 1] if i - start > 0 else ('...' if start != 0 else ''))

        if len(center) == 2:
            center = ' ' + center

        output += f'{center : ^5}│'

    output += f'{("..." if upper <= len(tape) else "" ) : ^5}\n'

    for _ in iterations():
        output += '─────┴'

    output += '─────\n'

    for i in iterations():
        cell_header = f'{"▲" if i - 1 == selected_pos and i != 0 else "": ^5}'
        output += f'{cell_header} '

    output += ' ' * 5 + '\n'
    return output

def visualize(tape: list, selected_pos: int = -1, start: int = 0, cells: int = 0) -> None:
    print(visualize_str(tape, selected_pos, start, cells))

if __name__ == '__main__':
    visualize([1, 2, 38, 4, 255, 9, 8, 7, 6], selected_pos=5, start=2, cells=6)
