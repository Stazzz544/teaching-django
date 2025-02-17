import React, { useEffect, useState } from "react";

// Определяем тип данных, которые ожидаем получить с сервера
interface Product {
  id: number;
  title: string;
  content: string;
  price: string;
  image: string | null;
}

const ProductList: React.FC = () => {
  // Состояние для хранения списка продуктов
  const [products, setProducts] = useState<Product[]>([]);
  // Состояние для отслеживания загрузки данных
  const [loading, setLoading] = useState<boolean>(true);
  // Состояние для обработки ошибок
  const [error, setError] = useState<string | null>(null);

  // Функция для получения данных с сервера
  const fetchProducts = async () => {
    try {
      const response = await fetch("http://127.0.0.1:8000/get/"); // Укажите ваш эндпоинт
      if (!response.ok) {
        throw new Error("Ошибка при загрузке данных");
      }
      const data: any = await response.json();
      console.log(data.products);
      setProducts(data.products); // Предполагаем, что данные возвращаются в формате { products: Product[] }
      setLoading(false);
    } catch (err) {
      setError(err instanceof Error ? err.message : "Произошла ошибка");
      setLoading(false);
    }
  };

  // Загружаем данные при монтировании компонента
  useEffect(() => {
    fetchProducts();
  }, []);

  // Отображаем состояние загрузки
  if (loading) {
    return <div>Загрузка...</div>;
  }

  // Отображаем ошибку, если она есть
  if (error) {
    return <div>Ошибка: {error}</div>;
  }

  // Отображаем список продуктов
  return (
    <div>
      <h1>Список продуктов</h1>
      <ul>
        {products &&
          products.map((product) => (
            <li key={product.id}>
              <h2>{product.title}</h2>
              <p>{product.content}</p>
              <p>Цена: {product.price}</p>
              {product.image && (
                <img
                  src={product.image}
                  alt={product.title}
                  style={{ maxWidth: "100px" }}
                />
              )}
            </li>
          ))}
      </ul>
    </div>
  );
};

export default ProductList;
