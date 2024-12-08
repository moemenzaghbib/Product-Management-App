<template>
  <div v-if="isVisible" class="modal-overlay">
    <div class="modal">
      <h3>{{ selectedProduct ? 'Update' : 'Add' }} Product</h3>
      <form @submit.prevent="handleSubmit">
        <input v-model="productData.name" placeholder="Product Name" required />
        <input v-model="productData.price" type="number" placeholder="Price" required />
        <textarea v-model="productData.description" placeholder="Description"></textarea>
        <input v-model="productData.stock" type="number" placeholder="Stock" required />
        <button type="submit">{{ selectedProduct ? 'Update' : 'Add' }} Product</button>
      </form>
      <button @click="closeModal">Close</button>
    </div>
  </div>
</template>

<script>
import { ref, watch } from 'vue';
import { addProduct, updateProduct } from '../productApi';
import { useToast } from 'vue-toastification';

export default {
  props: {
    isVisible: Boolean,
    selectedProduct: Object,
  },
  emits: ['close', 'productAdded'],
  setup(props, { emit }) {
    const toast = useToast();
    const productData = ref({
      name: '',
      price: '',
      description: '',
      stock: '',
    });

    watch(() => props.selectedProduct, (newProduct) => {
      if (newProduct) {
        productData.value = { ...newProduct };
      } else {
        productData.value = {
          name: '',
          price: '',
          description: '',
          stock: '',
        };
      }
    });

    const closeModal = () => {
      emit('close');
      productData.value = {
      name: '',
      price: '',
      description: '',
      stock: '',
    };
    };

    const handleSubmit = async () => {
      try {
        if (props.selectedProduct) {
          await updateProduct(props.selectedProduct.id, productData.value);
          toast.success('Product updated successfully!');
        } else {
          await addProduct(productData.value);
          toast.success('Product added successfully!');
        }
        emit('productAdded');
        closeModal();
      } catch (error) {
        toast.error('Error handling product.');
      }
    };

    return {
      productData,
      closeModal,
      handleSubmit,
    };
  },
};
</script>

<style scoped src="../assets/styles/productAddModal.css"></style>
