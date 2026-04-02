import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import time
import random
import threading


def linear_sort(arr, ascending=False):
    n = len(arr)
    arr_2 = [0] * n
    arr_copy = arr.copy()
    
    if ascending:
        compare = lambda x, y: x < y
        replace_with = max(arr_copy) + 1
    else:
        compare = lambda x, y: x > y
        replace_with = min(arr_copy) - 1
    
    for i in range(n):
        extremum_idx = 0
        extremum_val = arr_copy[0]
        
        for j in range(1, n):
            if compare(arr_copy[j], extremum_val):
                extremum_val = arr_copy[j]
                extremum_idx = j                

        
        if ascending:
            arr_2[i] = extremum_val
        else:
            arr_2[i] = extremum_val
        
        arr_copy[extremum_idx] = replace_with
    
    return arr_2

def linear_sort_no_arr(arr, ascending=True):
    n = len(arr)
    result = arr.copy()
    
    for i in range(n):
        extremum_idx = i
        for j in range(i + 1, n):
            if ascending:
                if result[j] < result[extremum_idx]:
                    extremum_idx = j
            else:
                if result[j] > result[extremum_idx]:
                    extremum_idx = j
        
        if extremum_idx != i:
            result[i], result[extremum_idx] = result[extremum_idx], result[i]
    
    return result


def bubble_sort(arr, ascending=True):   
    n = len(arr)
    result = arr.copy()
    
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            if ascending:
                if result[j] > result[j + 1]:
                    result[j], result[j + 1] = result[j + 1], result[j]
                    swapped = True
            else:
                if result[j] < result[j + 1]:
                    result[j], result[j + 1] = result[j + 1], result[j]
                    swapped = True
        
        if not swapped:
            break
    
    return result


def shuttle_sort(arr, ascending=True):    
    n = len(arr)
    result = arr.copy()
    
    for i in range(1, n):
        j = i
        while j > 0:
            if ascending:
                if result[j] < result[j - 1]:
                    result[j], result[j - 1] = result[j - 1], result[j]
                    j -= 1
                else:
                    break
            else:
                if result[j] > result[j - 1]:
                    result[j], result[j - 1] = result[j - 1], result[j]
                    j -= 1
                else:
                    break
    
    return result


def insertion_sort(arr, ascending=True):
    n = len(arr)
    result = arr.copy()
    
    for i in range(1, n):
        key = result[i]
        j = i - 1
        
        if ascending:
            while j >= 0 and result[j] > key:
                result[j + 1] = result[j]
                j -= 1
        else:
            while j >= 0 and result[j] < key:
                result[j + 1] = result[j]
                j -= 1
        
        result[j + 1] = key
    
    return result

class SortingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Сортировка массива")
        self.root.geometry("900x650")
        self.root.resizable(True, True)
        
        self.original_array = []
        self.current_array = []
        self.sort_methods = {
            '1': {'name': "Линейный выбор (с вспомогательным массивом)", 'func': linear_sort},
            '2': {'name': "Метод минимального/максимального элемента", 'func': linear_sort_no_arr},
            '3': {'name': "Метод 'пузырька'", 'func': bubble_sort},
            '4': {'name': "Челночная сортировка", 'func': shuttle_sort},
            '5': {'name': "Сортировка вставками", 'func': insertion_sort}
        }
               
        self.create_widgets()
        
    def create_widgets(self):        
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
                
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(0, weight=1)
        main_frame.rowconfigure(3, weight=1)
                
        generate_frame = ttk.LabelFrame(main_frame, text="Генерация массива", padding="10")
        generate_frame.grid(row=0, column=0, sticky=(tk.W, tk.E), pady=(0, 10))
        
        ttk.Label(generate_frame, text="Размер массива:").grid(row=0, column=0, padx=(0, 5))
        self.size_var = tk.IntVar(value=100)
        self.size_spinbox = ttk.Spinbox(generate_frame, from_=100, to=10000, textvariable=self.size_var, width=10)
        self.size_spinbox.grid(row=0, column=1, padx=(0, 20))
        
        self.generate_btn = ttk.Button(generate_frame, text="Сгенерировать массив", command=self.generate_array)
        self.generate_btn.grid(row=0, column=2, padx=(0, 20))
        
        ttk.Label(generate_frame, text="Статус:").grid(row=0, column=3, padx=(0, 5))
        self.array_status = ttk.Label(generate_frame, text="Не сгенерирован", foreground="red")
        self.array_status.grid(row=0, column=4, sticky=tk.W)
                
        params_frame = ttk.LabelFrame(main_frame, text="Параметры сортировки", padding="10")
        params_frame.grid(row=1, column=0, sticky=(tk.W, tk.E), pady=(0, 10))
        
        ttk.Label(params_frame, text="Направление сортировки:").grid(row=0, column=0, padx=(0, 10))
        self.sort_direction = tk.StringVar(value="asc")
        ttk.Radiobutton(params_frame, text="По возрастанию", variable=self.sort_direction, value="asc").grid(row=0, column=1, padx=(0, 10))
        ttk.Radiobutton(params_frame, text="По убыванию", variable=self.sort_direction, value="desc").grid(row=0, column=2)
                
        method_frame = ttk.LabelFrame(main_frame, text="Выбор метода сортировки", padding="10")
        method_frame.grid(row=2, column=0, sticky=(tk.W, tk.E), pady=(0, 10))
                
        self.method_var = tk.StringVar(value="1")
        
        row = 0
        col = 0
        for key, method in self.sort_methods.items():
            ttk.Radiobutton(method_frame, text=method['name'], variable=self.method_var, value=key).grid(
                row=row, column=col, sticky=tk.W, padx=(0, 20), pady=5
            )
            col += 1
            if col > 1:
                col = 0
                row += 1
                
        self.sort_btn = ttk.Button(method_frame, text="ВЫПОЛНИТЬ СОРТИРОВКУ", command=self.sort_array, style="Accent.TButton")
        self.sort_btn.grid(row=row+1, column=0, columnspan=2, pady=(10, 0))
        
        style = ttk.Style()
        style.configure("Accent.TButton", font=("Arial", 10, "bold"))
        
        results_frame = ttk.LabelFrame(main_frame, text="Результаты", padding="10")
        results_frame.grid(row=3, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        results_frame.columnconfigure(0, weight=1)
        results_frame.rowconfigure(0, weight=1)
                
        self.text_output = scrolledtext.ScrolledText(results_frame, height=15, wrap=tk.WORD, font=("Courier", 10))
        self.text_output.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        self.status_var = tk.StringVar(value="Готов к работе")
        status_bar = ttk.Label(main_frame, textvariable=self.status_var, relief=tk.SUNKEN, anchor=tk.W)
        status_bar.grid(row=4, column=0, sticky=(tk.W, tk.E), pady=(10, 0))
        
    def log(self, message, clear=False):        
        if clear:
            self.text_output.delete(1.0, tk.END)
        self.text_output.insert(tk.END, message + "\n")
        self.text_output.see(tk.END)
        self.root.update_idletasks()
        
    def update_status(self, message):        
        self.status_var.set(message)
        self.root.update_idletasks()
        
    def generate_array(self):        
        try:
            size = self.size_var.get()
            
            self.original_array = [random.randint(1, 10000) for _ in range(size)]
            self.array_status.config(text=f"Сгенерирован ({size} элементов)", foreground="green")
            
            self.log(f"✓ Сгенерирован массив из {size} элементов", clear=True)
            self.log(f"Первые 20 элементов: {self.original_array[:20]}")
            if size > 20:
                self.log(f"... и еще {size - 20} элементов")
            
            self.update_status(f"Массив из {size} элементов успешно сгенерирован")
            
        except Exception as e:
            messagebox.showerror("Ошибка", f"Ошибка при генерации массива: {e}")
    
    def sort_array(self):        
        if not self.original_array:
            messagebox.showwarning("Предупреждение", "Сначала сгенерируйте массив!")
            return
                
        method_key = self.method_var.get()
        method_name = self.sort_methods[method_key]['name']
        sort_func = self.sort_methods[method_key]['func']
        
        ascending = self.sort_direction.get() == 'asc'
        direction_text = "возрастанию" if ascending else "убыванию"
                
        self.log(f"\n{'='*60}", clear=True)
        self.log(f"ЗАПУСК СОРТИРОВКИ")
        self.log(f"{'='*60}")
        self.log(f"Метод: {method_name}")
        self.log(f"Направление: по {direction_text}")
        self.log(f"Размер массива: {len(self.original_array)} элементов")
        self.log("")
                
        self.sort_btn.config(state=tk.DISABLED)
        self.generate_btn.config(state=tk.DISABLED)        
        thread = threading.Thread(target=self.run_sorting, args=(sort_func, method_name, ascending))
        thread.daemon = True
        thread.start()
    
    def run_sorting(self, sort_func, method_name, ascending):        
        self.update_status(f"Выполняется сортировка методом: {method_name}...")

        sorted_array = sort_func(self.original_array, ascending)        
                        
        self.log(f"✓ Сортировка завершена!")
        self.log(f"")
        self.log(f"{'='*60}")
        self.log(f"РЕЗУЛЬТАТЫ")
        self.log(f"{'='*60}")

        self.log(f"")
        self.log(f"Оригинальный массив (первые 20 элементов):")
        self.log(f"{self.original_array[:20]}")
        self.log(f"")
        self.log(f"Отсортированный массив (первые 20 элементов):")
        self.log(f"{sorted_array[:20]}")
        if len(sorted_array) > 20:
            self.log(f"... и еще {len(sorted_array) - 20} элементов")
                
        is_correct = True
        for i in range(len(sorted_array) - 1):
            if ascending:
                if sorted_array[i] > sorted_array[i + 1]:
                    is_correct = False
                    break
            else:
                if sorted_array[i] < sorted_array[i + 1]:
                    is_correct = False
                    break
        
        if is_correct:
            self.log(f"")
            self.log(f"✓ ПРОВЕРКА: Массив отсортирован КОРРЕКТНО!")
        else:
            self.log(f"")
            self.log(f"✗ ПРОВЕРКА: ОШИБКА! Массив отсортирован НЕПРАВИЛЬНО!")
        
        self.log(f"\n{'='*60}")
        
        self.sort_btn.config(state=tk.NORMAL)
        self.generate_btn.config(state=tk.NORMAL)


def main():
    root = tk.Tk()
    app = SortingApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
