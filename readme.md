#Django test app

This follows the pluralsight django fundamentals tutorial from [Reindert-Jan Ekker]
(https://app.pluralsight.com/profile/author/reindertjan-ekker). A **great** tutor!

**Don´t forget**:
The tutorial doesn´t include
on_delete=models.CASCADE
which is required as of django 2.0
It was the default before, but now needs to be explicit.  See /player/models for example usage.