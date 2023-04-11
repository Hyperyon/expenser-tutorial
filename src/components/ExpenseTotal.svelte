<script type="text/javascript">
	import store, {totalTweenStore} from '../shared/ExpenseStore.js'

	let total = 0
	store.subscribe(data =>{
		total = data.reduce((acc,curr) =>{
			return curr.subtotal + acc
		},0)

		totalTweenStore.set(total)
	})
</script>

<div class="card" style="width: 18rem;">
  <div class="card-body">
    <h5 class="card-title">Total</h5>
    <h6 class="card-subtitle mb-2 text-muted">All expenses</h6>
    <p class="card-text">Total : {$totalTweenStore}</p>
  </div>
</div>