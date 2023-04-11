<script type="text/javascript">
	import {onMount} from "svelte"
	import ExpenseTable from './components/ExpenseTable.svelte'
	import ExpenseCreate from './components/ExpenseCreate.svelte'
	import ExpenseTotal from './components/ExpenseTotal.svelte'
	import store from './shared/ExpenseStore.js'

	let expenses = []
	let expensesFirestore = []

	store.subscribe(data =>{
		expenses = data
	})	
</script>


<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css"
		integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">

<style type="text/css">
	h1{color:purple;}
</style>


<h1>Expense tracker</h1>
<ExpenseTotal />
<ExpenseCreate/>
<ExpenseTable {expenses}/>