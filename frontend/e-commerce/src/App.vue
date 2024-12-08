<template>
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Your Vue.js App</title>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css" rel="stylesheet">
  </head>

  <div id="main-page">
    <h1>Welcome to the Products Management Dashboard</h1>
    <ProductList />
  </div>
</template>

<script>
import ProductList from './components/ProductList.vue';

export default {
  name: 'MainPage',
  components: {
    ProductList,
  },
};
</script>

<style scoped>
#template {
  background-color: #f4f6f9;
}

#main-page {
  padding: 20px;
  text-align: center;
  font-family: 'Arial', sans-serif;
}

h1 {
  font-size: 36px;
  color: #333;
  font-weight: bold;
  margin-bottom: 30px;
  letter-spacing: 2px;
}

h1::after {
  content: "";
  display: block;
  width: 80px;
  height: 3px;
  background-color: #44a889;
  margin: 20px auto;
}
</style>
