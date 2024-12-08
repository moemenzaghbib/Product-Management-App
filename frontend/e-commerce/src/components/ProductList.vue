<template>
  <div class="product-list">
    <div class="filters">
      <div class="stock-switch-wrapper">
        <label for="inStock">In Stock</label>
        <input
          type="checkbox"
          id="inStock"
          v-model="inStock"
          @change="loadProducts"
          class="stock-switch"
        />
      </div>
      <button @click="openAddModal" class="addProd" aria-label="add-product">
        <i class="fas fa-plus"></i> Add Product
      </button>
    </div>

    <div v-if="isLoading" class="loader">
      <p>Loading products...</p>
    </div>

    <table v-if="!isLoading">
      <thead>
        <tr>
          <th>Name</th>
          <th>Description</th>
          <th>Price</th>
          <th>Stock</th>
          <th>Actions</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="product in products" :key="product.id">
          <td>{{ product.name }}</td>
          <td>{{ product.description }}</td>
          <td>{{ product.price }}</td>
          <td>
            <button
              :class="product.stock === 0 ? 'out-of-stock' : 'in-stock'"
            >
              <i :class="product.stock === 0 ? 'fas fa-times-circle' : 'fas fa-check-circle'"></i>
              {{ product.stock === 0 ? 'Out of Stock' : `In Stock (${product.stock})` }}
            </button>
          </td>
          <td class="action-buttons">
            <button @click="openModal(product)" class="update-btn">
              <i class="fas fa-pencil-alt"></i> Update
            </button>
            <button @click="deleteProduct(product.id)" class="delete-btn">
              <i class="fas fa-trash-alt"></i> Delete
            </button>
          </td>
        </tr>
      </tbody>
    </table>

    <div v-if="!isLoading" class="pagination">
      <button
        :disabled="currentPage === 1"
        @click="changePage(currentPage - 1)"
        class="previous"
        aria-label="previous-page"
      >
        <i class="fas fa-chevron-left"></i> 
      </button>

      <span>Page {{ currentPage }} of {{ totalPages }}</span>

      <button
        :disabled="!hasMorePages"
        @click="changePage(currentPage + 1)"
        class="next"
        aria-label="next-page"
      >
        <i class="fas fa-chevron-right"></i> 
      </button>
    </div>

    <ProductAddModal
      :isVisible="isModalVisible"
      :selectedProduct="selectedProduct"
      @close="closeModal"
      @productAdded="refreshProducts"
    />
  </div>
</template>

<script>
import { ref } from "vue";
import { fetchPaginatedProducts, deleteProductById } from "../productApi"; 
import ProductAddModal from "./ProductAddModal.vue";
import { useToast } from "vue-toastification";

export default {
  components: { ProductAddModal },
  setup() {
    const toast = useToast();
    const products = ref([]);
    const currentPage = ref(1);
    const totalPages = ref(1);
    const inStock = ref(false);
    const isLoading = ref(false);
    const hasMorePages = ref(true);
    const isModalVisible = ref(false);
    const selectedProduct = ref(null);

    const loadProducts = async () => {
      try {
        isLoading.value = true;
        const { data, has_more, total_pages } = await fetchPaginatedProducts(
          currentPage.value,
          5,
          inStock.value
        );
        products.value = data;
        hasMorePages.value = has_more;
        totalPages.value = total_pages;

        setTimeout(() => {
          isLoading.value = false;
        }, 2000);
      } catch (error) {
        toast.error("Failed to fetch products.");
        isLoading.value = false;
      }
    };

    const changePage = (page) => {
      if (page < 1 || page > totalPages.value) return; 
      currentPage.value = page;
      loadProducts();
    };

    const openModal = (product) => {
      selectedProduct.value = product;
      isModalVisible.value = true;
    };

    const openAddModal = () => {
      selectedProduct.value = null;
      isModalVisible.value = true;
    };

    const closeModal = () => {
      isModalVisible.value = false;
    };

    const deleteProduct = async (id) => {
      try {
        await deleteProductById(id);
        toast.success("Product deleted successfully!");
        loadProducts();
      } catch (error) {
        toast.error("Error deleting product.");
      }
    };

    const refreshProducts = () => {
      loadProducts();
    };

    loadProducts();

    return {
      products,
      currentPage,
      totalPages,
      inStock,
      isLoading,
      hasMorePages,
      isModalVisible,
      selectedProduct,
      loadProducts,
      changePage,
      openModal,
      openAddModal,
      closeModal,
      deleteProduct,
      refreshProducts,
    };
  },
};
</script>

<style scoped src="../assets/styles/productList.css"></style>

