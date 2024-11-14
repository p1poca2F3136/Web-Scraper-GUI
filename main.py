from imports import *


def scrape_data():
    url = url_entry.get()
    element = element_entry.get()

    try:
        response = requests.get(url)
        response.raise_for_status() 
        soup = BeautifulSoup(response.text, 'html.parser')
        
        results = soup.find_all(element)
        data = [result.get_text() for result in results]
        
        result_text.set("\n".join(data) if data else "Nenhum dado encontrado.")
    except Exception as e:
        messagebox.showerror("Erro", f"Falha ao realizar o scraping: {e}")


root = tk.Tk()
root.title("Web Scraper Simples")

tk.Label(root, text="URL do site:").grid(row=0, column=0, padx=10, pady=10)
url_entry = tk.Entry(root, width=50)
url_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Elemento HTML (ex: h1, p, div):").grid(row=1, column=0, padx=10, pady=10)
element_entry = tk.Entry(root, width=20)
element_entry.grid(row=1, column=1, padx=10, pady=10)

result_text = tk.StringVar()
tk.Label(root, textvariable=result_text, wraplength=500).grid(row=3, column=0, columnspan=2, padx=10, pady=10)

scrape_button = tk.Button(root, text="Realizar Scraping", command=scrape_data)
scrape_button.grid(row=2, column=0, columnspan=2, pady=10)

root.mainloop()
