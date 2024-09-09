Question 1: By default, are Django signals executed synchronously or asynchronously?
Answer:
By default, Django signals are executed synchronously. This means that the signal handler is executed in the same request/response cycle and must complete before the request finishes.

Code Example:
I have created a signal that includes a delay (time.sleep(3)) to simulate a time-consuming task.
We can then trigger the signal from a Django view and measure the time taken for the view to complete.

For this, need to run api : localhost:8000\myapp\create


2. Do Django signals run in the same thread as the caller?
Answer:
Yes, by default, Django signals run in the same thread as the caller.

Code Example:
We have printed the current thread name both in the view (the caller) and in the signal handler.
By comparing the thread names, we can verify that they are running in the same thread.

For this, need to run api : localhost:8000\myapp\test-thread

Both the view and the signal handler are running in the same thread (MainThread), proving that Django signals run in the same thread as the caller by default.

3: By default, do Django signals run in the same database transaction as the caller?
Answer:
Yes, by default, Django signals run in the same database transaction as the caller. If the transaction is rolled back, the signal's actions are also rolled back.

Code Example:
We'll create a signal that inserts a new record in the database.
We'll simulate a rollback in the view by raising an exception and check if the signal's database action is also rolled back.

For this, need to run api : localhost:8000\myapp\test-transaction



Rectangle class:

For getting rectangular dimensions need to pass : localhost:8000\myapp\test-rectangle

When we visit this url, it will instantiate a Rectangle object with a length of 10 and width of 5.
The view will iterate over the Rectangle object and return a JSON response like:
eg:
{
    "rectangle": [
        {"length": 10},
        {"width": 5}
    ]
}