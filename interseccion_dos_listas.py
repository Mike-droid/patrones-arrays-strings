def interseccion_dos_listas(first_list, second_list):
    if len(first_list) == 0 or len(second_list) == 0:
        return []

    lista_resultado = []

    i, j = 0, 0
    while i < len(first_list) and j < len(second_list):
        start1, end1 = first_list[i]
        start2, end2 = second_list[j]

        # Find the intersection between two intervals
        if end1 >= start2 and end2 >= start1:
            start_inter = max(start1, start2)
            end_inter = min(end1, end2)
            lista_resultado.append([start_inter, end_inter])

        # Move to the next interval in the list that finishes first
        if end1 < end2:
            i += 1
        else:
            j += 1

    return lista_resultado

if __name__ == "__main__":
    print(interseccion_dos_listas([[0,2],[5,10],[13,23],[24,25]], [[1,5],[8,12],[15,24],[25,26]]))  # Expected: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
    print(interseccion_dos_listas([[1,3],[5,9]], []))  # Expected: []
