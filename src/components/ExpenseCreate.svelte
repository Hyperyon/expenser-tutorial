<script type="text/javascript">

	import store from '../shared/ExpenseStore.js'
	import expenseService from '../shared/ExpenseService.js'

	let date, paymentType, category,quantity
	let amount = "00.00"
	$: subtotal = amount*quantity

	function createExpense() {
		let newExpense = {
			date,
			paymentType,
			category,
			amount:parseFloat(amount),
			quantity,
			subtotal
		} 

	expenseService.create(newExpense)
	.then(Object =>{
		store.update(data =>{
		newExpense.id = Object[0].id;
		return [newExpense,...data];
		})
		initForm();
	})
  	
	}

function initForm() {
	date = getCurrentDate()
	paymentType = "cash"
	category = "rent"
	amount = "00.00"
	quantity = 1
}

 function getCurrentDate() {
    var today = new Date();
    return (
      today.getFullYear() +
      "-" +
      ("0" + (today.getMonth() + 1)).slice(-2) +
      "-" +
      ("0" + today.getDate()).slice(-2)
    );
  }

  initForm();
</script>

<style type="text/css">
	
</style>

<form on:submit|preventDefault={createExpense}>
	<div class="form-group">
		<label for="date">Date</label>
		<input 
		type="date" 
		class="form-control" 
		id="date" 
		placeholder="dd/mm/yyyy" 
		bind:value={date}>
	</div>
	  <div class="form-group">
    <label for="paymentType">Payment type</label>
    <select class="form-control" id="paymentType" bind:value={paymentType}>
      <option value="cash">cash</option>
      <option value="card">card</option>
      <option value="direct-debit">direct debit</option>
      <option value="cheque">cheque</option>
    </select>
  </div>
  <div class="form-group">
    <label for="category">Category</label>
    <select class="form-control" id="category" bind:value={category}>
      <option value="rent">rent</option>
      <option value="electricity">electricity</option>
      <option value="food">food</option>
      <option value="phone">phone</option>
      <option value="gas">gas</option>
    </select>
  </div>
  <div class="form-group">
    <label for="amount">Amount</label>
    <input
      type="text"
      class="form-control"
      id="amount"
      placeholder="amount"
      bind:value={amount} />
  </div>
  <div class="form-group">
    <label for="quantity">Quantity</label>
    <input
      type="number"
      class="form-control"
      id="quantity"
      placeholder="quantity"
      bind:value={quantity} />
  </div>

  <button type="submit" class="btn btn-success">create</button>
</form>