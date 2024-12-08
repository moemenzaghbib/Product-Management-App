import axios from 'axios';

const API_URL = 'http://127.0.0.1:8000/api/products/';

export const getProducts = async () => {
  try {
    const response = await axios.get(API_URL);
    return response.data;
  } catch (error) {
    console.error('Error fetching products:', error);
    throw error;
  }
};

export const addProduct = async (productData) => {
  try {
    const response = await axios.post(API_URL, productData);
    return response.data;
  } catch (error) {
    console.error('Error adding product:', error);
    throw error;
  }
};

export const updateProduct = async (id, updatedData) => {
  try {
    const response = await axios.put(`${API_URL}${id}/`, updatedData);
    return response.data;
  } catch (error) {
    console.error('Error updating product:', error);
    throw error;
  }
};

export const deleteProduct = async (id) => {
  try {
    await axios.delete(`${API_URL}${id}/`);
  } catch (error) {
    console.error('Error deleting product:', error);
    throw error;
  }
};

export const fetchPaginatedProducts = async (page = 1, pageSize = 5, inStock = false) => {
  try {
    const response = await axios.get(API_URL+`paginated-products/`, {
      params: {
        page,
        page_size: pageSize,
        in_stock: inStock,
      },
    });
    return response.data;
  } catch (error) {
    console.error('Error fetching products:', error);
    throw error;
  }
};

export const deleteProductById = async (id) => {
  try {
    await axios.delete(`${API_URL}${id}/`);
  } catch (error) {
    console.error('Error deleting product:', error);
    throw error;
  }
};
