from connstans import MATERIALS
from menu import show_menu, select_material
from validation import input_length, input_width, input_thickness, input_quantity
from operations import calc_mass, thickness_class

def main() -> None:
    print("Расчёт массы партии листов")
    
    while True:
        show_menu()
        choice = select_material()
        
        if choice is None:
            print("Работа завершена.")
            break

        material_name, density = MATERIALS[choice]
        print(f"\nВыбран материал: {material_name}, ρ = {density} кг/м³")

        # Ввод данных
        L = input_length()
        W = input_width()
        t = input_thickness()
        q = input_quantity()

        # Расчёт
        mass = calc_mass(L, W, t, density, q)
        t_class = thickness_class(t)

        # Вывод
        print("\n--- РЕЗУЛЬТАТ ---")
        print(f"Материал:        {material_name}")
        print(f"Размеры:         {L} x {W} м, толщина {t} мм")
        print(f"Количество:      {q} шт.")
        print(f"Масса партии:    {mass:.3f} кг")
        print(f"Класс толщины:   {t_class}")
        print("-" * 25)

if __name__ == "__main__":
    main()