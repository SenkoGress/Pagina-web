document.addEventListener('DOMContentLoaded', () => {
    const productList = document.getElementById('product-list');
    const cartList = document.getElementById('cart-list');
    const totalPrice = document.getElementById('total-price');
    const cartCount = document.getElementById('cart-count');

    let cart = [];
    let total = 0;

    // PRODUCTOS
    const products = [
        { name: "Producto 3", price: 10.00, img: "https://cdnx.jumpseller.com/espesales/image/23072873/resize/640/640?1654524722" },
        { name: "Producto 4", price: 15.00, img: "https://i.blogs.es/a82edb/comino1/840_560.jpg" },
        { name: "Producto 5", price: 20.00, img: "https://i.blogs.es/78b1e0/foto-apertura-cilantro/1366_2000.jpg" },
        { name: "Producto 6", price: 25.00, img: "https://i.blogs.es/84fe19/clavo-de-olor-min/1366_2000.jpg" },
        { name: "Producto 7", price: 30.00, img: "https://media.glamour.mx/photos/6513e7e7bb61961b5a2c3c46/master/pass/menta-en-el-shampoo.jpg" },
        { name: "Producto 8", price: 35.00, img: "https://mejorconsalud.as.com/wp-content/uploads/2016/05/rama-perejil-fresco.jpg" }
        // DE AQUI PARA ABAJO SE PUEDEN AGREGAR MAS PRODUCTOS
    ];

    // RENDERIZAR PRODUCTOS
    products.forEach(product => {
        const col = document.createElement('div');
        col.className = 'col-md-3 product-container';
        col.innerHTML = `
            <div class="card product-card">
                <img src="${product.img}" class="card-img-top product-image" alt="${product.name}">
                <div class="card-body">
                    <h5 class="card-title">${product.name}</h5>
                    <p class="card-text">$${product.price.toFixed(2)}</p>
                    <button class="btn btn-primary add-to-cart" data-name="${product.name}" data-price="${product.price.toFixed(2)}">Añadir al Carrito</button>
                </div>
            </div>`;
        productList.appendChild(col);
    });

    // EVENTO AÑADIR AL CARRITO
    document.querySelectorAll('.add-to-cart').forEach(button => {
        button.addEventListener('click', event => {
            const name = event.target.getAttribute('data-name');
            const price = parseFloat(event.target.getAttribute('data-price'));

            // BUSCAR SI EL PRODUCTO YA ESTA EN EL CARRITO
            const existingProduct = cart.find(item => item.name === name);
            if (existingProduct) {
                existingProduct.quantity += 1;
                existingProduct.totalPrice += price;
            } else {
                cart.push({ name, price, quantity: 1, totalPrice: price });
            }

            total += price;
            updateCart();
        });
    });

    // EVENTO BOTÓN COMPRAR
    document.querySelector('.buy-button').addEventListener('click', () => {
        alert('Compra realizada con éxito!'); // Mensaje de compra exitosa

        // Reiniciar el carrito y total
        cart = [];
        total = 0;
        updateCart();
    });

    // ACTUALIZAR CARRO DE COMPRAS
    function updateCart() {
        cartList.innerHTML = ''; // Limpiar lista de carrito
        cart.forEach((item, index) => {
            const listItem = document.createElement('li');
            listItem.className = 'list-group-item d-flex justify-content-between align-items-center';
            listItem.innerHTML = `
                ${item.name} - $${item.totalPrice.toFixed(2)} 
                <span class="badge badge-primary badge-pill">${item.quantity}</span>
                <button class="btn btn-danger btn-sm remove-from-cart" data-index="${index}">Eliminar</button>
            `;
            cartList.appendChild(listItem);
        });

        totalPrice.textContent = total.toFixed(2);
        cartCount.textContent = cart.reduce((count, item) => count + item.quantity, 0);

        // EVENTO ELIMINAR DEL CARRITO
        document.querySelectorAll('.remove-from-cart').forEach(button => {
            button.addEventListener('click', event => {
                const index = parseInt(event.target.getAttribute('data-index'));
                const product = cart[index];
                total -= product.price;

                if (product.quantity > 1) {
                    product.quantity -= 1;
                    product.totalPrice -= product.price;
                } else {
                    cart.splice(index, 1);
                }

                updateCart();
            });
        });
    }

    // IR AL CARRITO
    document.querySelector('a[href="#carrito-section"]').addEventListener('click', (event) => {
        event.preventDefault();
        document.querySelector('#carrito-section').scrollIntoView({
            behavior: 'smooth'
        });
    });
});
