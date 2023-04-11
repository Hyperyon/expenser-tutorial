<script type="text/javascript">
	
import {fade} from 'svelte/transition'
import {createEventDispatcher} from "svelte"
const dispatch = createEventDispatcher()
export let exp


const fadeOptions = {
duration:150
}

let isInEditMode = false
let itemEdit = {
	date:"",
	paymentType:"",
	category:"",
	amount: 0,
	quantity:1,
	subtotal:0
}

function toggleEdit(exp) {
	isInEditMode = !isInEditMode
		if(isInEditMode){
		itemEdit = {...exp}
	}
}

function handleInput(event, fieldName) {
	itemEdit[fieldName] = event.target.value
	if(fieldName === "quantity" || fieldName === "amount")
		itemEdit["subtotal"] = itemEdit["quantity"]*itemEdit["amount"]
}

function save() {
	dispatch("expense-update",itemEdit)
	isInEditMode = false
}

function deleteExpense(expense) {
	dispatch("expense-delete",expense)
}

</script>


<style type="text/css">
	.action{
		font-size: 14px;
		margin-right: 3px;
		cursor: pointer;
	}

	.id{
		font-size: 12px;
	}

</style>

{#if !isInEditMode}
  <tr transition:fade={fadeOptions}>
      <td scope="row">{exp.id}</td>
      <td>{exp.date}</td>
      <td>{exp.paymentType}</td>
      <td>{exp.category}</td>
      <td>{exp.amount}</td>
      <td>{exp.quantity}</td>
      <td>{exp.subtotal}</td>
      <td>
      	<span class="action" on:click={() => toggleEdit(exp)}>edit</span> 
      	<span class="action" on:click={() => deleteExpense(exp)}>delete</span></td>
    </tr>
{:else}
<tr>
	<th scope="row">
		<span class="id">{exp.id}</span>
	</th>
	<td>
		<input type="date" value={exp.date} on:change={ev => handleInput(ev, 'date')}>
	</td>
	<td>
		<input type="text" value={exp.paymentType} on:input={ev => handleInput(ev, 'paymentType')}>
	</td>
	<td>
		<input type="text" value={exp.category} on:input={ev => handleInput(ev, 'category')}>
	</td>
	<td>
		<input type="number" value={exp.amount} on:change={ev => handleInput(ev, 'amount')}>
	</td>
	<td>
		<input type="number" value={exp.quantity} on:change={ev => handleInput(ev, 'quantity')}>
	</td>
	<td>{exp.subtotal}</td>
<td>
      	<span class="action" on:click={save}>save</span> 
      	<span class="action" on:click={toggleEdit.bind(this)}>cancel</span>
</td>

</tr>
{/if}