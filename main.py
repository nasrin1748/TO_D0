from pyscript import display,HTML
def dual_prompt():
    # DOM Display
    dom_prompt = f"""
    <div id="prompt-container" style="margin: 20px 0;padding: 15px;
        border-radius: 8px;
        background-color: #f5f5f5;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
        <div style="margin-bottom: 15px;">
        <input type="text" id="itemInput" placeholder="Enter item" style="
                    padding: 8px;
                    border: 1px solid #ddd;
                    border-radius: 4px;
                    margin-right: 10px;
                    width: 200px;">
        <button onclick="addItem()"  style="
                    padding: 8px 15px;
                    background-color: #4CAF50;
                    color: white;
                    border: none;
                    border-radius: 4px;
                    cursor: pointer;">Add Item</button>
        <ul id="itemList"></ul>
    </div>
  

    <script>
    function addItem() {{
            const itemInput = document.getElementById('itemInput');
            const itemList = document.getElementById('itemList');
            const newItem = itemInput.value;

            if (newItem){{
                const li = document.createElement('li');
                li.textContent = newItem;
                li.onclick = () => deleteItem(li);
                itemList.appendChild(li);
                itemInput.value = '';
            }}
        }}

        function deleteItem(element) {{
            element.parentNode.removeChild(element);
        }}
    </script>
    """
    display(HTML(dom_prompt))

# Call the function
#result = dual_prompt()
