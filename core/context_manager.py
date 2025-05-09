from datetime import datetime, timedelta

class AdvancedContextManager:
    def __init__(self, context_timeout_minutes=10):
        self.user_contexts = {}
        self.context_timeout = timedelta(minutes=context_timeout_minutes)

    def get_context(self, user_id):
        context = self.user_contexts.get(user_id)
        if context and not self._is_expired(context):
            return context
        else:
            self.clear_context(user_id)
            return None

    def update_context(self, user_id, intent=None, stage=None, extra_data=None):
        if user_id not in self.user_contexts:
            self.user_contexts[user_id] = {}

        context = self.user_contexts[user_id]
        
        # اطمینان از اینکه intent از نوع string باشه
        if isinstance(intent, dict):
            intent = intent.get("intent", "unknown")
        
        if intent is not None:
            context["intent"] = intent
        if stage is not None:
            context["stage"] = stage
        if extra_data is not None:
            context["extra"] = extra_data
        context["last_updated"] = datetime.now()

    def clear_context(self, user_id):
        if user_id in self.user_contexts:
            del self.user_contexts[user_id]

    def _is_expired(self, context):
        last_updated = context.get("last_updated")
        if last_updated is None:
            return True
        return datetime.now() - last_updated > self.context_timeout
