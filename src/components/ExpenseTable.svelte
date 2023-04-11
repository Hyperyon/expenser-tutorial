<script>

  import ExpenseRow from './ExpenseRow.svelte'
  import expenseService from '../shared/ExpenseService.js'
  import store from '../shared/ExpenseStore.js'
  export let expenses
  console.log(expenses)

function updateExpense(event) {
  const updatedExpense = event.detail
  expenseService
  .update(updatedExpense)
  .then(()=>{
    store.update(data =>{
      const idx = data.findIndex(expense => expense.id === updatedExpense.id)
      data[idx] = updatedExpense
      return [...data]
    })
  })

}

function deleteExpense(event) {
  console.log('pouet')
  const deletedExpense = event.detail
  expenseService.delet(deletedExpense)
  .then(()=>{
    store.update(data =>{
      data = data.filter(expense => expense.id !== deletedExpense.id)
      return [...data]
    })
  })
}

</script>

<style>
</style>

<table class="table table-striped">
  <thead>
    <tr>
      <th scope="col">#</th>
      <th scope="col">Date</th>
      <th scope="col">Payment type</th>
      <th scope="col">Category</th>
      <th scope="col">Amount</th>
      <th scope="col">Quantity</th>
      <th scope="col">Subtotal</th>
      <th scope="col"></th>
    </tr>
  </thead>
  <tbody>
    {#each expenses as exp}
    <ExpenseRow {exp} on:expense-update={updateExpense} on:expense-delete={deleteExpense}/>
    {/each}
  </tbody>
</table>