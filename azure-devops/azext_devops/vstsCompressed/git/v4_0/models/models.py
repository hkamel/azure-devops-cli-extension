# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# Generated file, DO NOT EDIT
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------------------------


from msrest.serialization import Model



class AssociatedWorkItem(Model):
    """AssociatedWorkItem.

    :param assigned_to:
    :type assigned_to: str
    :param id:
    :type id: int
    :param state:
    :type state: str
    :param title:
    :type title: str
    :param url: REST url
    :type url: str
    :param web_url:
    :type web_url: str
    :param work_item_type:
    :type work_item_type: str
    """

    _attribute_map = {
        'assigned_to': {'key': 'assignedTo', 'type': 'str'},
        'id': {'key': 'id', 'type': 'int'},
        'state': {'key': 'state', 'type': 'str'},
        'title': {'key': 'title', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'},
        'web_url': {'key': 'webUrl', 'type': 'str'},
        'work_item_type': {'key': 'workItemType', 'type': 'str'}
    }

    def __init__(self, assigned_to=None, id=None, state=None, title=None, url=None, web_url=None, work_item_type=None):
        super(AssociatedWorkItem, self).__init__()
        self.assigned_to = assigned_to
        self.id = id
        self.state = state
        self.title = title
        self.url = url
        self.web_url = web_url
        self.work_item_type = work_item_type



class Attachment(Model):
    """Attachment.

    :param _links:
    :type _links: :class:`ReferenceLinks <git.v4_0.models.ReferenceLinks>`
    :param author: The person that uploaded this attachment
    :type author: :class:`IdentityRef <git.v4_0.models.IdentityRef>`
    :param content_hash: Content hash of on-disk representation of file content. Its calculated by the server by using SHA1 hash function.
    :type content_hash: str
    :param created_date: The time the attachment was uploaded
    :type created_date: datetime
    :param description: The description of the attachment, can be null.
    :type description: str
    :param display_name: The display name of the attachment, can't be null or empty.
    :type display_name: str
    :param id: Id of the code review attachment
    :type id: int
    :param properties:
    :type properties: :class:`object <git.v4_0.models.object>`
    :param url: The url to download the content of the attachment
    :type url: str
    """

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'author': {'key': 'author', 'type': 'IdentityRef'},
        'content_hash': {'key': 'contentHash', 'type': 'str'},
        'created_date': {'key': 'createdDate', 'type': 'iso-8601'},
        'description': {'key': 'description', 'type': 'str'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'id': {'key': 'id', 'type': 'int'},
        'properties': {'key': 'properties', 'type': 'object'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, _links=None, author=None, content_hash=None, created_date=None, description=None, display_name=None, id=None, properties=None, url=None):
        super(Attachment, self).__init__()
        self._links = _links
        self.author = author
        self.content_hash = content_hash
        self.created_date = created_date
        self.description = description
        self.display_name = display_name
        self.id = id
        self.properties = properties
        self.url = url



class Change(Model):
    """Change.

    :param change_type:
    :type change_type: object
    :param item:
    :type item: object
    :param new_content:
    :type new_content: :class:`ItemContent <git.v4_0.models.ItemContent>`
    :param source_server_item:
    :type source_server_item: str
    :param url:
    :type url: str
    """

    _attribute_map = {
        'change_type': {'key': 'changeType', 'type': 'object'},
        'item': {'key': 'item', 'type': 'object'},
        'new_content': {'key': 'newContent', 'type': 'ItemContent'},
        'source_server_item': {'key': 'sourceServerItem', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, change_type=None, item=None, new_content=None, source_server_item=None, url=None):
        super(Change, self).__init__()
        self.change_type = change_type
        self.item = item
        self.new_content = new_content
        self.source_server_item = source_server_item
        self.url = url



class Comment(Model):
    """Comment.

    :param _links:
    :type _links: :class:`ReferenceLinks <git.v4_0.models.ReferenceLinks>`
    :param author: The author of the pull request comment.
    :type author: :class:`IdentityRef <git.v4_0.models.IdentityRef>`
    :param comment_type: Determines what kind of comment when it was created.
    :type comment_type: object
    :param content: The comment's content.
    :type content: str
    :param id: The pull request comment id. It always starts from 1.
    :type id: int
    :param is_deleted: Marks if this comment was soft-deleted.
    :type is_deleted: bool
    :param last_content_updated_date: The date a comment content was last updated.
    :type last_content_updated_date: datetime
    :param last_updated_date: The date a comment was last updated.
    :type last_updated_date: datetime
    :param parent_comment_id: The pull request comment id of the parent comment. This is used for replies
    :type parent_comment_id: int
    :param published_date: The date a comment was first published.
    :type published_date: datetime
    :param users_liked: A list of the users who've liked this comment.
    :type users_liked: list of :class:`IdentityRef <git.v4_0.models.IdentityRef>`
    """

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'author': {'key': 'author', 'type': 'IdentityRef'},
        'comment_type': {'key': 'commentType', 'type': 'object'},
        'content': {'key': 'content', 'type': 'str'},
        'id': {'key': 'id', 'type': 'int'},
        'is_deleted': {'key': 'isDeleted', 'type': 'bool'},
        'last_content_updated_date': {'key': 'lastContentUpdatedDate', 'type': 'iso-8601'},
        'last_updated_date': {'key': 'lastUpdatedDate', 'type': 'iso-8601'},
        'parent_comment_id': {'key': 'parentCommentId', 'type': 'int'},
        'published_date': {'key': 'publishedDate', 'type': 'iso-8601'},
        'users_liked': {'key': 'usersLiked', 'type': '[IdentityRef]'}
    }

    def __init__(self, _links=None, author=None, comment_type=None, content=None, id=None, is_deleted=None, last_content_updated_date=None, last_updated_date=None, parent_comment_id=None, published_date=None, users_liked=None):
        super(Comment, self).__init__()
        self._links = _links
        self.author = author
        self.comment_type = comment_type
        self.content = content
        self.id = id
        self.is_deleted = is_deleted
        self.last_content_updated_date = last_content_updated_date
        self.last_updated_date = last_updated_date
        self.parent_comment_id = parent_comment_id
        self.published_date = published_date
        self.users_liked = users_liked



class CommentIterationContext(Model):
    """CommentIterationContext.

    :param first_comparing_iteration: First comparing iteration Id. Minimum value is 1.
    :type first_comparing_iteration: int
    :param second_comparing_iteration: Second comparing iteration Id. Minimum value is 1.
    :type second_comparing_iteration: int
    """

    _attribute_map = {
        'first_comparing_iteration': {'key': 'firstComparingIteration', 'type': 'int'},
        'second_comparing_iteration': {'key': 'secondComparingIteration', 'type': 'int'}
    }

    def __init__(self, first_comparing_iteration=None, second_comparing_iteration=None):
        super(CommentIterationContext, self).__init__()
        self.first_comparing_iteration = first_comparing_iteration
        self.second_comparing_iteration = second_comparing_iteration



class CommentPosition(Model):
    """CommentPosition.

    :param line: Position line starting with one.
    :type line: int
    :param offset: Position offset starting with zero.
    :type offset: int
    """

    _attribute_map = {
        'line': {'key': 'line', 'type': 'int'},
        'offset': {'key': 'offset', 'type': 'int'}
    }

    def __init__(self, line=None, offset=None):
        super(CommentPosition, self).__init__()
        self.line = line
        self.offset = offset



class CommentThread(Model):
    """CommentThread.

    :param _links:
    :type _links: :class:`ReferenceLinks <git.v4_0.models.ReferenceLinks>`
    :param comments: A list of the comments.
    :type comments: list of :class:`Comment <git.v4_0.models.Comment>`
    :param id: The comment thread id.
    :type id: int
    :param is_deleted: Specify if the thread is deleted which happens when all comments are deleted
    :type is_deleted: bool
    :param last_updated_date: The time this thread was last updated.
    :type last_updated_date: datetime
    :param properties: A list of (optional) thread properties.
    :type properties: :class:`object <git.v4_0.models.object>`
    :param published_date: The time this thread was published.
    :type published_date: datetime
    :param status: The status of the comment thread.
    :type status: object
    :param thread_context: Specify thread context such as position in left/right file.
    :type thread_context: :class:`CommentThreadContext <git.v4_0.models.CommentThreadContext>`
    """

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'comments': {'key': 'comments', 'type': '[Comment]'},
        'id': {'key': 'id', 'type': 'int'},
        'is_deleted': {'key': 'isDeleted', 'type': 'bool'},
        'last_updated_date': {'key': 'lastUpdatedDate', 'type': 'iso-8601'},
        'properties': {'key': 'properties', 'type': 'object'},
        'published_date': {'key': 'publishedDate', 'type': 'iso-8601'},
        'status': {'key': 'status', 'type': 'object'},
        'thread_context': {'key': 'threadContext', 'type': 'CommentThreadContext'}
    }

    def __init__(self, _links=None, comments=None, id=None, is_deleted=None, last_updated_date=None, properties=None, published_date=None, status=None, thread_context=None):
        super(CommentThread, self).__init__()
        self._links = _links
        self.comments = comments
        self.id = id
        self.is_deleted = is_deleted
        self.last_updated_date = last_updated_date
        self.properties = properties
        self.published_date = published_date
        self.status = status
        self.thread_context = thread_context



class CommentThreadContext(Model):
    """CommentThreadContext.

    :param file_path: File path relative to the root of the repository. It's up to the client to use any path format.
    :type file_path: str
    :param left_file_end: Position of last character of the comment in left file.
    :type left_file_end: :class:`CommentPosition <git.v4_0.models.CommentPosition>`
    :param left_file_start: Position of first character of the comment in left file.
    :type left_file_start: :class:`CommentPosition <git.v4_0.models.CommentPosition>`
    :param right_file_end: Position of last character of the comment in right file.
    :type right_file_end: :class:`CommentPosition <git.v4_0.models.CommentPosition>`
    :param right_file_start: Position of first character of the comment in right file.
    :type right_file_start: :class:`CommentPosition <git.v4_0.models.CommentPosition>`
    """

    _attribute_map = {
        'file_path': {'key': 'filePath', 'type': 'str'},
        'left_file_end': {'key': 'leftFileEnd', 'type': 'CommentPosition'},
        'left_file_start': {'key': 'leftFileStart', 'type': 'CommentPosition'},
        'right_file_end': {'key': 'rightFileEnd', 'type': 'CommentPosition'},
        'right_file_start': {'key': 'rightFileStart', 'type': 'CommentPosition'}
    }

    def __init__(self, file_path=None, left_file_end=None, left_file_start=None, right_file_end=None, right_file_start=None):
        super(CommentThreadContext, self).__init__()
        self.file_path = file_path
        self.left_file_end = left_file_end
        self.left_file_start = left_file_start
        self.right_file_end = right_file_end
        self.right_file_start = right_file_start



class CommentTrackingCriteria(Model):
    """CommentTrackingCriteria.

    :param first_comparing_iteration: The first comparing iteration being viewed. Threads will be tracked if this is greater than 0.
    :type first_comparing_iteration: int
    :param orig_left_file_end: Original position of last character of the comment in left file.
    :type orig_left_file_end: :class:`CommentPosition <git.v4_0.models.CommentPosition>`
    :param orig_left_file_start: Original position of first character of the comment in left file.
    :type orig_left_file_start: :class:`CommentPosition <git.v4_0.models.CommentPosition>`
    :param orig_right_file_end: Original position of last character of the comment in right file.
    :type orig_right_file_end: :class:`CommentPosition <git.v4_0.models.CommentPosition>`
    :param orig_right_file_start: Original position of first character of the comment in right file.
    :type orig_right_file_start: :class:`CommentPosition <git.v4_0.models.CommentPosition>`
    :param second_comparing_iteration: The second comparing iteration being viewed. Threads will be tracked if this is greater than 0.
    :type second_comparing_iteration: int
    """

    _attribute_map = {
        'first_comparing_iteration': {'key': 'firstComparingIteration', 'type': 'int'},
        'orig_left_file_end': {'key': 'origLeftFileEnd', 'type': 'CommentPosition'},
        'orig_left_file_start': {'key': 'origLeftFileStart', 'type': 'CommentPosition'},
        'orig_right_file_end': {'key': 'origRightFileEnd', 'type': 'CommentPosition'},
        'orig_right_file_start': {'key': 'origRightFileStart', 'type': 'CommentPosition'},
        'second_comparing_iteration': {'key': 'secondComparingIteration', 'type': 'int'}
    }

    def __init__(self, first_comparing_iteration=None, orig_left_file_end=None, orig_left_file_start=None, orig_right_file_end=None, orig_right_file_start=None, second_comparing_iteration=None):
        super(CommentTrackingCriteria, self).__init__()
        self.first_comparing_iteration = first_comparing_iteration
        self.orig_left_file_end = orig_left_file_end
        self.orig_left_file_start = orig_left_file_start
        self.orig_right_file_end = orig_right_file_end
        self.orig_right_file_start = orig_right_file_start
        self.second_comparing_iteration = second_comparing_iteration



class FileContentMetadata(Model):
    """FileContentMetadata.

    :param content_type:
    :type content_type: str
    :param encoding:
    :type encoding: int
    :param extension:
    :type extension: str
    :param file_name:
    :type file_name: str
    :param is_binary:
    :type is_binary: bool
    :param is_image:
    :type is_image: bool
    :param vs_link:
    :type vs_link: str
    """

    _attribute_map = {
        'content_type': {'key': 'contentType', 'type': 'str'},
        'encoding': {'key': 'encoding', 'type': 'int'},
        'extension': {'key': 'extension', 'type': 'str'},
        'file_name': {'key': 'fileName', 'type': 'str'},
        'is_binary': {'key': 'isBinary', 'type': 'bool'},
        'is_image': {'key': 'isImage', 'type': 'bool'},
        'vs_link': {'key': 'vsLink', 'type': 'str'}
    }

    def __init__(self, content_type=None, encoding=None, extension=None, file_name=None, is_binary=None, is_image=None, vs_link=None):
        super(FileContentMetadata, self).__init__()
        self.content_type = content_type
        self.encoding = encoding
        self.extension = extension
        self.file_name = file_name
        self.is_binary = is_binary
        self.is_image = is_image
        self.vs_link = vs_link



class GitAnnotatedTag(Model):
    """GitAnnotatedTag.

    :param message: Tagging Message
    :type message: str
    :param name:
    :type name: str
    :param object_id:
    :type object_id: str
    :param tagged_by: User name, Email and date of tagging
    :type tagged_by: :class:`GitUserDate <git.v4_0.models.GitUserDate>`
    :param tagged_object: Tagged git object
    :type tagged_object: :class:`GitObject <git.v4_0.models.GitObject>`
    :param url:
    :type url: str
    """

    _attribute_map = {
        'message': {'key': 'message', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'object_id': {'key': 'objectId', 'type': 'str'},
        'tagged_by': {'key': 'taggedBy', 'type': 'GitUserDate'},
        'tagged_object': {'key': 'taggedObject', 'type': 'GitObject'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, message=None, name=None, object_id=None, tagged_by=None, tagged_object=None, url=None):
        super(GitAnnotatedTag, self).__init__()
        self.message = message
        self.name = name
        self.object_id = object_id
        self.tagged_by = tagged_by
        self.tagged_object = tagged_object
        self.url = url



class GitAsyncRefOperation(Model):
    """GitAsyncRefOperation.

    :param _links:
    :type _links: :class:`ReferenceLinks <git.v4_0.models.ReferenceLinks>`
    :param detailed_status:
    :type detailed_status: :class:`GitAsyncRefOperationDetail <git.v4_0.models.GitAsyncRefOperationDetail>`
    :param parameters:
    :type parameters: :class:`GitAsyncRefOperationParameters <git.v4_0.models.GitAsyncRefOperationParameters>`
    :param status:
    :type status: object
    :param url:
    :type url: str
    """

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'detailed_status': {'key': 'detailedStatus', 'type': 'GitAsyncRefOperationDetail'},
        'parameters': {'key': 'parameters', 'type': 'GitAsyncRefOperationParameters'},
        'status': {'key': 'status', 'type': 'object'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, _links=None, detailed_status=None, parameters=None, status=None, url=None):
        super(GitAsyncRefOperation, self).__init__()
        self._links = _links
        self.detailed_status = detailed_status
        self.parameters = parameters
        self.status = status
        self.url = url



class GitAsyncRefOperationDetail(Model):
    """GitAsyncRefOperationDetail.

    :param conflict:
    :type conflict: bool
    :param current_commit_id:
    :type current_commit_id: str
    :param failure_message:
    :type failure_message: str
    :param progress:
    :type progress: float
    :param status:
    :type status: object
    :param timedout:
    :type timedout: bool
    """

    _attribute_map = {
        'conflict': {'key': 'conflict', 'type': 'bool'},
        'current_commit_id': {'key': 'currentCommitId', 'type': 'str'},
        'failure_message': {'key': 'failureMessage', 'type': 'str'},
        'progress': {'key': 'progress', 'type': 'float'},
        'status': {'key': 'status', 'type': 'object'},
        'timedout': {'key': 'timedout', 'type': 'bool'}
    }

    def __init__(self, conflict=None, current_commit_id=None, failure_message=None, progress=None, status=None, timedout=None):
        super(GitAsyncRefOperationDetail, self).__init__()
        self.conflict = conflict
        self.current_commit_id = current_commit_id
        self.failure_message = failure_message
        self.progress = progress
        self.status = status
        self.timedout = timedout



class GitAsyncRefOperationParameters(Model):
    """GitAsyncRefOperationParameters.

    :param generated_ref_name:
    :type generated_ref_name: str
    :param onto_ref_name:
    :type onto_ref_name: str
    :param repository:
    :type repository: :class:`GitRepository <git.v4_0.models.GitRepository>`
    :param source:
    :type source: :class:`GitAsyncRefOperationSource <git.v4_0.models.GitAsyncRefOperationSource>`
    """

    _attribute_map = {
        'generated_ref_name': {'key': 'generatedRefName', 'type': 'str'},
        'onto_ref_name': {'key': 'ontoRefName', 'type': 'str'},
        'repository': {'key': 'repository', 'type': 'GitRepository'},
        'source': {'key': 'source', 'type': 'GitAsyncRefOperationSource'}
    }

    def __init__(self, generated_ref_name=None, onto_ref_name=None, repository=None, source=None):
        super(GitAsyncRefOperationParameters, self).__init__()
        self.generated_ref_name = generated_ref_name
        self.onto_ref_name = onto_ref_name
        self.repository = repository
        self.source = source



class GitAsyncRefOperationSource(Model):
    """GitAsyncRefOperationSource.

    :param commit_list:
    :type commit_list: list of :class:`GitCommitRef <git.v4_0.models.GitCommitRef>`
    :param pull_request_id:
    :type pull_request_id: int
    """

    _attribute_map = {
        'commit_list': {'key': 'commitList', 'type': '[GitCommitRef]'},
        'pull_request_id': {'key': 'pullRequestId', 'type': 'int'}
    }

    def __init__(self, commit_list=None, pull_request_id=None):
        super(GitAsyncRefOperationSource, self).__init__()
        self.commit_list = commit_list
        self.pull_request_id = pull_request_id



class GitBlobRef(Model):
    """GitBlobRef.

    :param _links:
    :type _links: :class:`ReferenceLinks <git.v4_0.models.ReferenceLinks>`
    :param object_id: SHA1 hash of git object
    :type object_id: str
    :param size: Size of blob content (in bytes)
    :type size: long
    :param url:
    :type url: str
    """

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'object_id': {'key': 'objectId', 'type': 'str'},
        'size': {'key': 'size', 'type': 'long'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, _links=None, object_id=None, size=None, url=None):
        super(GitBlobRef, self).__init__()
        self._links = _links
        self.object_id = object_id
        self.size = size
        self.url = url



class GitBranchStats(Model):
    """GitBranchStats.

    :param ahead_count:
    :type ahead_count: int
    :param behind_count:
    :type behind_count: int
    :param commit:
    :type commit: :class:`GitCommitRef <git.v4_0.models.GitCommitRef>`
    :param is_base_version:
    :type is_base_version: bool
    :param name:
    :type name: str
    """

    _attribute_map = {
        'ahead_count': {'key': 'aheadCount', 'type': 'int'},
        'behind_count': {'key': 'behindCount', 'type': 'int'},
        'commit': {'key': 'commit', 'type': 'GitCommitRef'},
        'is_base_version': {'key': 'isBaseVersion', 'type': 'bool'},
        'name': {'key': 'name', 'type': 'str'}
    }

    def __init__(self, ahead_count=None, behind_count=None, commit=None, is_base_version=None, name=None):
        super(GitBranchStats, self).__init__()
        self.ahead_count = ahead_count
        self.behind_count = behind_count
        self.commit = commit
        self.is_base_version = is_base_version
        self.name = name



class GitCherryPick(GitAsyncRefOperation):
    """GitCherryPick.

    :param _links:
    :type _links: :class:`ReferenceLinks <git.v4_0.models.ReferenceLinks>`
    :param detailed_status:
    :type detailed_status: :class:`GitAsyncRefOperationDetail <git.v4_0.models.GitAsyncRefOperationDetail>`
    :param parameters:
    :type parameters: :class:`GitAsyncRefOperationParameters <git.v4_0.models.GitAsyncRefOperationParameters>`
    :param status:
    :type status: object
    :param url:
    :type url: str
    :param cherry_pick_id:
    :type cherry_pick_id: int
    """

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'detailed_status': {'key': 'detailedStatus', 'type': 'GitAsyncRefOperationDetail'},
        'parameters': {'key': 'parameters', 'type': 'GitAsyncRefOperationParameters'},
        'status': {'key': 'status', 'type': 'object'},
        'url': {'key': 'url', 'type': 'str'},
        'cherry_pick_id': {'key': 'cherryPickId', 'type': 'int'}
    }

    def __init__(self, _links=None, detailed_status=None, parameters=None, status=None, url=None, cherry_pick_id=None):
        super(GitCherryPick, self).__init__(_links=_links, detailed_status=detailed_status, parameters=parameters, status=status, url=url)
        self.cherry_pick_id = cherry_pick_id



class GitCommitChanges(Model):
    """GitCommitChanges.

    :param change_counts:
    :type change_counts: dict
    :param changes:
    :type changes: list of :class:`object <git.v4_0.models.object>`
    """

    _attribute_map = {
        'change_counts': {'key': 'changeCounts', 'type': '{int}'},
        'changes': {'key': 'changes', 'type': '[object]'}
    }

    def __init__(self, change_counts=None, changes=None):
        super(GitCommitChanges, self).__init__()
        self.change_counts = change_counts
        self.changes = changes



class GitCommitDiffs(Model):
    """GitCommitDiffs.

    :param ahead_count:
    :type ahead_count: int
    :param all_changes_included:
    :type all_changes_included: bool
    :param base_commit:
    :type base_commit: str
    :param behind_count:
    :type behind_count: int
    :param change_counts:
    :type change_counts: dict
    :param changes:
    :type changes: list of :class:`object <git.v4_0.models.object>`
    :param common_commit:
    :type common_commit: str
    :param target_commit:
    :type target_commit: str
    """

    _attribute_map = {
        'ahead_count': {'key': 'aheadCount', 'type': 'int'},
        'all_changes_included': {'key': 'allChangesIncluded', 'type': 'bool'},
        'base_commit': {'key': 'baseCommit', 'type': 'str'},
        'behind_count': {'key': 'behindCount', 'type': 'int'},
        'change_counts': {'key': 'changeCounts', 'type': '{int}'},
        'changes': {'key': 'changes', 'type': '[object]'},
        'common_commit': {'key': 'commonCommit', 'type': 'str'},
        'target_commit': {'key': 'targetCommit', 'type': 'str'}
    }

    def __init__(self, ahead_count=None, all_changes_included=None, base_commit=None, behind_count=None, change_counts=None, changes=None, common_commit=None, target_commit=None):
        super(GitCommitDiffs, self).__init__()
        self.ahead_count = ahead_count
        self.all_changes_included = all_changes_included
        self.base_commit = base_commit
        self.behind_count = behind_count
        self.change_counts = change_counts
        self.changes = changes
        self.common_commit = common_commit
        self.target_commit = target_commit



class GitCommitRef(Model):
    """GitCommitRef.

    :param _links:
    :type _links: :class:`ReferenceLinks <git.v4_0.models.ReferenceLinks>`
    :param author:
    :type author: :class:`GitUserDate <git.v4_0.models.GitUserDate>`
    :param change_counts:
    :type change_counts: dict
    :param changes:
    :type changes: list of :class:`object <git.v4_0.models.object>`
    :param comment:
    :type comment: str
    :param comment_truncated:
    :type comment_truncated: bool
    :param commit_id:
    :type commit_id: str
    :param committer:
    :type committer: :class:`GitUserDate <git.v4_0.models.GitUserDate>`
    :param parents:
    :type parents: list of str
    :param remote_url:
    :type remote_url: str
    :param statuses:
    :type statuses: list of :class:`GitStatus <git.v4_0.models.GitStatus>`
    :param url:
    :type url: str
    :param work_items:
    :type work_items: list of :class:`ResourceRef <git.v4_0.models.ResourceRef>`
    """

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'author': {'key': 'author', 'type': 'GitUserDate'},
        'change_counts': {'key': 'changeCounts', 'type': '{int}'},
        'changes': {'key': 'changes', 'type': '[object]'},
        'comment': {'key': 'comment', 'type': 'str'},
        'comment_truncated': {'key': 'commentTruncated', 'type': 'bool'},
        'commit_id': {'key': 'commitId', 'type': 'str'},
        'committer': {'key': 'committer', 'type': 'GitUserDate'},
        'parents': {'key': 'parents', 'type': '[str]'},
        'remote_url': {'key': 'remoteUrl', 'type': 'str'},
        'statuses': {'key': 'statuses', 'type': '[GitStatus]'},
        'url': {'key': 'url', 'type': 'str'},
        'work_items': {'key': 'workItems', 'type': '[ResourceRef]'}
    }

    def __init__(self, _links=None, author=None, change_counts=None, changes=None, comment=None, comment_truncated=None, commit_id=None, committer=None, parents=None, remote_url=None, statuses=None, url=None, work_items=None):
        super(GitCommitRef, self).__init__()
        self._links = _links
        self.author = author
        self.change_counts = change_counts
        self.changes = changes
        self.comment = comment
        self.comment_truncated = comment_truncated
        self.commit_id = commit_id
        self.committer = committer
        self.parents = parents
        self.remote_url = remote_url
        self.statuses = statuses
        self.url = url
        self.work_items = work_items



class GitConflict(Model):
    """GitConflict.

    :param _links:
    :type _links: :class:`ReferenceLinks <git.v4_0.models.ReferenceLinks>`
    :param conflict_id:
    :type conflict_id: int
    :param conflict_path:
    :type conflict_path: str
    :param conflict_type:
    :type conflict_type: object
    :param merge_base_commit:
    :type merge_base_commit: :class:`GitCommitRef <git.v4_0.models.GitCommitRef>`
    :param merge_origin:
    :type merge_origin: :class:`GitMergeOriginRef <git.v4_0.models.GitMergeOriginRef>`
    :param merge_source_commit:
    :type merge_source_commit: :class:`GitCommitRef <git.v4_0.models.GitCommitRef>`
    :param merge_target_commit:
    :type merge_target_commit: :class:`GitCommitRef <git.v4_0.models.GitCommitRef>`
    :param resolution_error:
    :type resolution_error: object
    :param resolution_status:
    :type resolution_status: object
    :param resolved_by:
    :type resolved_by: :class:`IdentityRef <git.v4_0.models.IdentityRef>`
    :param resolved_date:
    :type resolved_date: datetime
    :param url:
    :type url: str
    """

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'conflict_id': {'key': 'conflictId', 'type': 'int'},
        'conflict_path': {'key': 'conflictPath', 'type': 'str'},
        'conflict_type': {'key': 'conflictType', 'type': 'object'},
        'merge_base_commit': {'key': 'mergeBaseCommit', 'type': 'GitCommitRef'},
        'merge_origin': {'key': 'mergeOrigin', 'type': 'GitMergeOriginRef'},
        'merge_source_commit': {'key': 'mergeSourceCommit', 'type': 'GitCommitRef'},
        'merge_target_commit': {'key': 'mergeTargetCommit', 'type': 'GitCommitRef'},
        'resolution_error': {'key': 'resolutionError', 'type': 'object'},
        'resolution_status': {'key': 'resolutionStatus', 'type': 'object'},
        'resolved_by': {'key': 'resolvedBy', 'type': 'IdentityRef'},
        'resolved_date': {'key': 'resolvedDate', 'type': 'iso-8601'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, _links=None, conflict_id=None, conflict_path=None, conflict_type=None, merge_base_commit=None, merge_origin=None, merge_source_commit=None, merge_target_commit=None, resolution_error=None, resolution_status=None, resolved_by=None, resolved_date=None, url=None):
        super(GitConflict, self).__init__()
        self._links = _links
        self.conflict_id = conflict_id
        self.conflict_path = conflict_path
        self.conflict_type = conflict_type
        self.merge_base_commit = merge_base_commit
        self.merge_origin = merge_origin
        self.merge_source_commit = merge_source_commit
        self.merge_target_commit = merge_target_commit
        self.resolution_error = resolution_error
        self.resolution_status = resolution_status
        self.resolved_by = resolved_by
        self.resolved_date = resolved_date
        self.url = url



class GitDeletedRepository(Model):
    """GitDeletedRepository.

    :param created_date:
    :type created_date: datetime
    :param deleted_by:
    :type deleted_by: :class:`IdentityRef <git.v4_0.models.IdentityRef>`
    :param deleted_date:
    :type deleted_date: datetime
    :param id:
    :type id: str
    :param name:
    :type name: str
    :param project:
    :type project: :class:`TeamProjectReference <git.v4_0.models.TeamProjectReference>`
    """

    _attribute_map = {
        'created_date': {'key': 'createdDate', 'type': 'iso-8601'},
        'deleted_by': {'key': 'deletedBy', 'type': 'IdentityRef'},
        'deleted_date': {'key': 'deletedDate', 'type': 'iso-8601'},
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'project': {'key': 'project', 'type': 'TeamProjectReference'}
    }

    def __init__(self, created_date=None, deleted_by=None, deleted_date=None, id=None, name=None, project=None):
        super(GitDeletedRepository, self).__init__()
        self.created_date = created_date
        self.deleted_by = deleted_by
        self.deleted_date = deleted_date
        self.id = id
        self.name = name
        self.project = project



class GitFilePathsCollection(Model):
    """GitFilePathsCollection.

    :param commit_id:
    :type commit_id: str
    :param paths:
    :type paths: list of str
    :param url:
    :type url: str
    """

    _attribute_map = {
        'commit_id': {'key': 'commitId', 'type': 'str'},
        'paths': {'key': 'paths', 'type': '[str]'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, commit_id=None, paths=None, url=None):
        super(GitFilePathsCollection, self).__init__()
        self.commit_id = commit_id
        self.paths = paths
        self.url = url



class GitForkOperationStatusDetail(Model):
    """GitForkOperationStatusDetail.

    :param all_steps: All valid steps for the forking process
    :type all_steps: list of str
    :param current_step: Index into AllSteps for the current step
    :type current_step: int
    :param error_message: Error message if the operation failed.
    :type error_message: str
    """

    _attribute_map = {
        'all_steps': {'key': 'allSteps', 'type': '[str]'},
        'current_step': {'key': 'currentStep', 'type': 'int'},
        'error_message': {'key': 'errorMessage', 'type': 'str'}
    }

    def __init__(self, all_steps=None, current_step=None, error_message=None):
        super(GitForkOperationStatusDetail, self).__init__()
        self.all_steps = all_steps
        self.current_step = current_step
        self.error_message = error_message



class GitForkSyncRequest(Model):
    """GitForkSyncRequest.

    :param _links: Collection of related links
    :type _links: :class:`ReferenceLinks <git.v4_0.models.ReferenceLinks>`
    :param detailed_status:
    :type detailed_status: :class:`GitForkOperationStatusDetail <git.v4_0.models.GitForkOperationStatusDetail>`
    :param operation_id: Unique identifier for the operation.
    :type operation_id: int
    :param source: Fully-qualified identifier for the source repository.
    :type source: :class:`GlobalGitRepositoryKey <git.v4_0.models.GlobalGitRepositoryKey>`
    :param source_to_target_refs: If supplied, the set of ref mappings to use when performing a "sync" or create. If missing, all refs will be synchronized.
    :type source_to_target_refs: list of :class:`SourceToTargetRef <git.v4_0.models.SourceToTargetRef>`
    :param status:
    :type status: object
    """

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'detailed_status': {'key': 'detailedStatus', 'type': 'GitForkOperationStatusDetail'},
        'operation_id': {'key': 'operationId', 'type': 'int'},
        'source': {'key': 'source', 'type': 'GlobalGitRepositoryKey'},
        'source_to_target_refs': {'key': 'sourceToTargetRefs', 'type': '[SourceToTargetRef]'},
        'status': {'key': 'status', 'type': 'object'}
    }

    def __init__(self, _links=None, detailed_status=None, operation_id=None, source=None, source_to_target_refs=None, status=None):
        super(GitForkSyncRequest, self).__init__()
        self._links = _links
        self.detailed_status = detailed_status
        self.operation_id = operation_id
        self.source = source
        self.source_to_target_refs = source_to_target_refs
        self.status = status



class GitForkSyncRequestParameters(Model):
    """GitForkSyncRequestParameters.

    :param source: Fully-qualified identifier for the source repository.
    :type source: :class:`GlobalGitRepositoryKey <git.v4_0.models.GlobalGitRepositoryKey>`
    :param source_to_target_refs: If supplied, the set of ref mappings to use when performing a "sync" or create. If missing, all refs will be synchronized.
    :type source_to_target_refs: list of :class:`SourceToTargetRef <git.v4_0.models.SourceToTargetRef>`
    """

    _attribute_map = {
        'source': {'key': 'source', 'type': 'GlobalGitRepositoryKey'},
        'source_to_target_refs': {'key': 'sourceToTargetRefs', 'type': '[SourceToTargetRef]'}
    }

    def __init__(self, source=None, source_to_target_refs=None):
        super(GitForkSyncRequestParameters, self).__init__()
        self.source = source
        self.source_to_target_refs = source_to_target_refs



class GitImportGitSource(Model):
    """GitImportGitSource.

    :param overwrite: Tells if this is a sync request or not
    :type overwrite: bool
    :param url: Url for the source repo
    :type url: str
    """

    _attribute_map = {
        'overwrite': {'key': 'overwrite', 'type': 'bool'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, overwrite=None, url=None):
        super(GitImportGitSource, self).__init__()
        self.overwrite = overwrite
        self.url = url



class GitImportRequest(Model):
    """GitImportRequest.

    :param _links:
    :type _links: :class:`ReferenceLinks <git.v4_0.models.ReferenceLinks>`
    :param detailed_status:
    :type detailed_status: :class:`GitImportStatusDetail <git.v4_0.models.GitImportStatusDetail>`
    :param import_request_id:
    :type import_request_id: int
    :param parameters: Parameters for creating an import request
    :type parameters: :class:`GitImportRequestParameters <git.v4_0.models.GitImportRequestParameters>`
    :param repository:
    :type repository: :class:`GitRepository <git.v4_0.models.GitRepository>`
    :param status:
    :type status: object
    :param url:
    :type url: str
    """

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'detailed_status': {'key': 'detailedStatus', 'type': 'GitImportStatusDetail'},
        'import_request_id': {'key': 'importRequestId', 'type': 'int'},
        'parameters': {'key': 'parameters', 'type': 'GitImportRequestParameters'},
        'repository': {'key': 'repository', 'type': 'GitRepository'},
        'status': {'key': 'status', 'type': 'object'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, _links=None, detailed_status=None, import_request_id=None, parameters=None, repository=None, status=None, url=None):
        super(GitImportRequest, self).__init__()
        self._links = _links
        self.detailed_status = detailed_status
        self.import_request_id = import_request_id
        self.parameters = parameters
        self.repository = repository
        self.status = status
        self.url = url



class GitImportRequestParameters(Model):
    """GitImportRequestParameters.

    :param delete_service_endpoint_after_import_is_done: Option to delete service endpoint when import is done
    :type delete_service_endpoint_after_import_is_done: bool
    :param git_source: Source for importing git repository
    :type git_source: :class:`GitImportGitSource <git.v4_0.models.GitImportGitSource>`
    :param service_endpoint_id: Service Endpoint for connection to external endpoint
    :type service_endpoint_id: str
    :param tfvc_source: Source for importing tfvc repository
    :type tfvc_source: :class:`GitImportTfvcSource <git.v4_0.models.GitImportTfvcSource>`
    """

    _attribute_map = {
        'delete_service_endpoint_after_import_is_done': {'key': 'deleteServiceEndpointAfterImportIsDone', 'type': 'bool'},
        'git_source': {'key': 'gitSource', 'type': 'GitImportGitSource'},
        'service_endpoint_id': {'key': 'serviceEndpointId', 'type': 'str'},
        'tfvc_source': {'key': 'tfvcSource', 'type': 'GitImportTfvcSource'}
    }

    def __init__(self, delete_service_endpoint_after_import_is_done=None, git_source=None, service_endpoint_id=None, tfvc_source=None):
        super(GitImportRequestParameters, self).__init__()
        self.delete_service_endpoint_after_import_is_done = delete_service_endpoint_after_import_is_done
        self.git_source = git_source
        self.service_endpoint_id = service_endpoint_id
        self.tfvc_source = tfvc_source



class GitImportStatusDetail(Model):
    """GitImportStatusDetail.

    :param all_steps:
    :type all_steps: list of str
    :param current_step:
    :type current_step: int
    :param error_message:
    :type error_message: str
    """

    _attribute_map = {
        'all_steps': {'key': 'allSteps', 'type': '[str]'},
        'current_step': {'key': 'currentStep', 'type': 'int'},
        'error_message': {'key': 'errorMessage', 'type': 'str'}
    }

    def __init__(self, all_steps=None, current_step=None, error_message=None):
        super(GitImportStatusDetail, self).__init__()
        self.all_steps = all_steps
        self.current_step = current_step
        self.error_message = error_message



class GitImportTfvcSource(Model):
    """GitImportTfvcSource.

    :param import_history: Set true to import History, false otherwise
    :type import_history: bool
    :param import_history_duration_in_days: Get history for last n days (max allowed value is 180 days)
    :type import_history_duration_in_days: int
    :param path: Path which we want to import (this can be copied from Path Control in Explorer)
    :type path: str
    """

    _attribute_map = {
        'import_history': {'key': 'importHistory', 'type': 'bool'},
        'import_history_duration_in_days': {'key': 'importHistoryDurationInDays', 'type': 'int'},
        'path': {'key': 'path', 'type': 'str'}
    }

    def __init__(self, import_history=None, import_history_duration_in_days=None, path=None):
        super(GitImportTfvcSource, self).__init__()
        self.import_history = import_history
        self.import_history_duration_in_days = import_history_duration_in_days
        self.path = path



class GitItemDescriptor(Model):
    """GitItemDescriptor.

    :param path: Path to item
    :type path: str
    :param recursion_level: Specifies whether to include children (OneLevel), all descendants (Full), or None
    :type recursion_level: object
    :param version: Version string (interpretation based on VersionType defined in subclass
    :type version: str
    :param version_options: Version modifiers (e.g. previous)
    :type version_options: object
    :param version_type: How to interpret version (branch,tag,commit)
    :type version_type: object
    """

    _attribute_map = {
        'path': {'key': 'path', 'type': 'str'},
        'recursion_level': {'key': 'recursionLevel', 'type': 'object'},
        'version': {'key': 'version', 'type': 'str'},
        'version_options': {'key': 'versionOptions', 'type': 'object'},
        'version_type': {'key': 'versionType', 'type': 'object'}
    }

    def __init__(self, path=None, recursion_level=None, version=None, version_options=None, version_type=None):
        super(GitItemDescriptor, self).__init__()
        self.path = path
        self.recursion_level = recursion_level
        self.version = version
        self.version_options = version_options
        self.version_type = version_type



class GitItemRequestData(Model):
    """GitItemRequestData.

    :param include_content_metadata: Whether to include metadata for all items
    :type include_content_metadata: bool
    :param include_links: Whether to include the _links field on the shallow references
    :type include_links: bool
    :param item_descriptors: Collection of items to fetch, including path, version, and recursion level
    :type item_descriptors: list of :class:`GitItemDescriptor <git.v4_0.models.GitItemDescriptor>`
    :param latest_processed_change: Whether to include shallow ref to commit that last changed each item
    :type latest_processed_change: bool
    """

    _attribute_map = {
        'include_content_metadata': {'key': 'includeContentMetadata', 'type': 'bool'},
        'include_links': {'key': 'includeLinks', 'type': 'bool'},
        'item_descriptors': {'key': 'itemDescriptors', 'type': '[GitItemDescriptor]'},
        'latest_processed_change': {'key': 'latestProcessedChange', 'type': 'bool'}
    }

    def __init__(self, include_content_metadata=None, include_links=None, item_descriptors=None, latest_processed_change=None):
        super(GitItemRequestData, self).__init__()
        self.include_content_metadata = include_content_metadata
        self.include_links = include_links
        self.item_descriptors = item_descriptors
        self.latest_processed_change = latest_processed_change



class GitMergeOriginRef(Model):
    """GitMergeOriginRef.

    :param pull_request_id:
    :type pull_request_id: int
    """

    _attribute_map = {
        'pull_request_id': {'key': 'pullRequestId', 'type': 'int'}
    }

    def __init__(self, pull_request_id=None):
        super(GitMergeOriginRef, self).__init__()
        self.pull_request_id = pull_request_id



class GitObject(Model):
    """GitObject.

    :param object_id: Git object id
    :type object_id: str
    :param object_type: Type of object (Commit, Tree, Blob, Tag)
    :type object_type: object
    """

    _attribute_map = {
        'object_id': {'key': 'objectId', 'type': 'str'},
        'object_type': {'key': 'objectType', 'type': 'object'}
    }

    def __init__(self, object_id=None, object_type=None):
        super(GitObject, self).__init__()
        self.object_id = object_id
        self.object_type = object_type



class GitPullRequest(Model):
    """GitPullRequest.

    :param _links:
    :type _links: :class:`ReferenceLinks <git.v4_0.models.ReferenceLinks>`
    :param artifact_id:
    :type artifact_id: str
    :param auto_complete_set_by:
    :type auto_complete_set_by: :class:`IdentityRef <git.v4_0.models.IdentityRef>`
    :param closed_by:
    :type closed_by: :class:`IdentityRef <git.v4_0.models.IdentityRef>`
    :param closed_date:
    :type closed_date: datetime
    :param code_review_id:
    :type code_review_id: int
    :param commits:
    :type commits: list of :class:`GitCommitRef <git.v4_0.models.GitCommitRef>`
    :param completion_options:
    :type completion_options: :class:`GitPullRequestCompletionOptions <git.v4_0.models.GitPullRequestCompletionOptions>`
    :param completion_queue_time:
    :type completion_queue_time: datetime
    :param created_by:
    :type created_by: :class:`IdentityRef <git.v4_0.models.IdentityRef>`
    :param creation_date:
    :type creation_date: datetime
    :param description:
    :type description: str
    :param fork_source:
    :type fork_source: :class:`GitForkRef <git.v4_0.models.GitForkRef>`
    :param labels:
    :type labels: list of :class:`WebApiTagDefinition <git.v4_0.models.WebApiTagDefinition>`
    :param last_merge_commit:
    :type last_merge_commit: :class:`GitCommitRef <git.v4_0.models.GitCommitRef>`
    :param last_merge_source_commit:
    :type last_merge_source_commit: :class:`GitCommitRef <git.v4_0.models.GitCommitRef>`
    :param last_merge_target_commit:
    :type last_merge_target_commit: :class:`GitCommitRef <git.v4_0.models.GitCommitRef>`
    :param merge_failure_message:
    :type merge_failure_message: str
    :param merge_failure_type:
    :type merge_failure_type: object
    :param merge_id:
    :type merge_id: str
    :param merge_options:
    :type merge_options: :class:`GitPullRequestMergeOptions <git.v4_0.models.GitPullRequestMergeOptions>`
    :param merge_status:
    :type merge_status: object
    :param pull_request_id:
    :type pull_request_id: int
    :param remote_url:
    :type remote_url: str
    :param repository:
    :type repository: :class:`GitRepository <git.v4_0.models.GitRepository>`
    :param reviewers:
    :type reviewers: list of :class:`IdentityRefWithVote <git.v4_0.models.IdentityRefWithVote>`
    :param source_ref_name:
    :type source_ref_name: str
    :param status:
    :type status: object
    :param supports_iterations:
    :type supports_iterations: bool
    :param target_ref_name:
    :type target_ref_name: str
    :param title:
    :type title: str
    :param url:
    :type url: str
    :param work_item_refs:
    :type work_item_refs: list of :class:`ResourceRef <git.v4_0.models.ResourceRef>`
    """

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'artifact_id': {'key': 'artifactId', 'type': 'str'},
        'auto_complete_set_by': {'key': 'autoCompleteSetBy', 'type': 'IdentityRef'},
        'closed_by': {'key': 'closedBy', 'type': 'IdentityRef'},
        'closed_date': {'key': 'closedDate', 'type': 'iso-8601'},
        'code_review_id': {'key': 'codeReviewId', 'type': 'int'},
        'commits': {'key': 'commits', 'type': '[GitCommitRef]'},
        'completion_options': {'key': 'completionOptions', 'type': 'GitPullRequestCompletionOptions'},
        'completion_queue_time': {'key': 'completionQueueTime', 'type': 'iso-8601'},
        'created_by': {'key': 'createdBy', 'type': 'IdentityRef'},
        'creation_date': {'key': 'creationDate', 'type': 'iso-8601'},
        'description': {'key': 'description', 'type': 'str'},
        'fork_source': {'key': 'forkSource', 'type': 'GitForkRef'},
        'labels': {'key': 'labels', 'type': '[WebApiTagDefinition]'},
        'last_merge_commit': {'key': 'lastMergeCommit', 'type': 'GitCommitRef'},
        'last_merge_source_commit': {'key': 'lastMergeSourceCommit', 'type': 'GitCommitRef'},
        'last_merge_target_commit': {'key': 'lastMergeTargetCommit', 'type': 'GitCommitRef'},
        'merge_failure_message': {'key': 'mergeFailureMessage', 'type': 'str'},
        'merge_failure_type': {'key': 'mergeFailureType', 'type': 'object'},
        'merge_id': {'key': 'mergeId', 'type': 'str'},
        'merge_options': {'key': 'mergeOptions', 'type': 'GitPullRequestMergeOptions'},
        'merge_status': {'key': 'mergeStatus', 'type': 'object'},
        'pull_request_id': {'key': 'pullRequestId', 'type': 'int'},
        'remote_url': {'key': 'remoteUrl', 'type': 'str'},
        'repository': {'key': 'repository', 'type': 'GitRepository'},
        'reviewers': {'key': 'reviewers', 'type': '[IdentityRefWithVote]'},
        'source_ref_name': {'key': 'sourceRefName', 'type': 'str'},
        'status': {'key': 'status', 'type': 'object'},
        'supports_iterations': {'key': 'supportsIterations', 'type': 'bool'},
        'target_ref_name': {'key': 'targetRefName', 'type': 'str'},
        'title': {'key': 'title', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'},
        'work_item_refs': {'key': 'workItemRefs', 'type': '[ResourceRef]'}
    }

    def __init__(self, _links=None, artifact_id=None, auto_complete_set_by=None, closed_by=None, closed_date=None, code_review_id=None, commits=None, completion_options=None, completion_queue_time=None, created_by=None, creation_date=None, description=None, fork_source=None, labels=None, last_merge_commit=None, last_merge_source_commit=None, last_merge_target_commit=None, merge_failure_message=None, merge_failure_type=None, merge_id=None, merge_options=None, merge_status=None, pull_request_id=None, remote_url=None, repository=None, reviewers=None, source_ref_name=None, status=None, supports_iterations=None, target_ref_name=None, title=None, url=None, work_item_refs=None):
        super(GitPullRequest, self).__init__()
        self._links = _links
        self.artifact_id = artifact_id
        self.auto_complete_set_by = auto_complete_set_by
        self.closed_by = closed_by
        self.closed_date = closed_date
        self.code_review_id = code_review_id
        self.commits = commits
        self.completion_options = completion_options
        self.completion_queue_time = completion_queue_time
        self.created_by = created_by
        self.creation_date = creation_date
        self.description = description
        self.fork_source = fork_source
        self.labels = labels
        self.last_merge_commit = last_merge_commit
        self.last_merge_source_commit = last_merge_source_commit
        self.last_merge_target_commit = last_merge_target_commit
        self.merge_failure_message = merge_failure_message
        self.merge_failure_type = merge_failure_type
        self.merge_id = merge_id
        self.merge_options = merge_options
        self.merge_status = merge_status
        self.pull_request_id = pull_request_id
        self.remote_url = remote_url
        self.repository = repository
        self.reviewers = reviewers
        self.source_ref_name = source_ref_name
        self.status = status
        self.supports_iterations = supports_iterations
        self.target_ref_name = target_ref_name
        self.title = title
        self.url = url
        self.work_item_refs = work_item_refs



class GitPullRequestChange(Model):
    """GitPullRequestChange.

    :param change_tracking_id: Id used to track files through multiple changes
    :type change_tracking_id: int
    """

    _attribute_map = {
        'change_tracking_id': {'key': 'changeTrackingId', 'type': 'int'}
    }

    def __init__(self, change_tracking_id=None):
        super(GitPullRequestChange, self).__init__()
        self.change_tracking_id = change_tracking_id



class GitPullRequestCommentThread(CommentThread):
    """GitPullRequestCommentThread.

    :param _links:
    :type _links: :class:`ReferenceLinks <git.v4_0.models.ReferenceLinks>`
    :param comments: A list of the comments.
    :type comments: list of :class:`Comment <git.v4_0.models.Comment>`
    :param id: The comment thread id.
    :type id: int
    :param is_deleted: Specify if the thread is deleted which happens when all comments are deleted
    :type is_deleted: bool
    :param last_updated_date: The time this thread was last updated.
    :type last_updated_date: datetime
    :param properties: A list of (optional) thread properties.
    :type properties: :class:`object <git.v4_0.models.object>`
    :param published_date: The time this thread was published.
    :type published_date: datetime
    :param status: The status of the comment thread.
    :type status: object
    :param thread_context: Specify thread context such as position in left/right file.
    :type thread_context: :class:`CommentThreadContext <git.v4_0.models.CommentThreadContext>`
    :param pull_request_thread_context: Extended context information unique to pull requests
    :type pull_request_thread_context: :class:`GitPullRequestCommentThreadContext <git.v4_0.models.GitPullRequestCommentThreadContext>`
    """

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'comments': {'key': 'comments', 'type': '[Comment]'},
        'id': {'key': 'id', 'type': 'int'},
        'is_deleted': {'key': 'isDeleted', 'type': 'bool'},
        'last_updated_date': {'key': 'lastUpdatedDate', 'type': 'iso-8601'},
        'properties': {'key': 'properties', 'type': 'object'},
        'published_date': {'key': 'publishedDate', 'type': 'iso-8601'},
        'status': {'key': 'status', 'type': 'object'},
        'thread_context': {'key': 'threadContext', 'type': 'CommentThreadContext'},
        'pull_request_thread_context': {'key': 'pullRequestThreadContext', 'type': 'GitPullRequestCommentThreadContext'}
    }

    def __init__(self, _links=None, comments=None, id=None, is_deleted=None, last_updated_date=None, properties=None, published_date=None, status=None, thread_context=None, pull_request_thread_context=None):
        super(GitPullRequestCommentThread, self).__init__(_links=_links, comments=comments, id=id, is_deleted=is_deleted, last_updated_date=last_updated_date, properties=properties, published_date=published_date, status=status, thread_context=thread_context)
        self.pull_request_thread_context = pull_request_thread_context



class GitPullRequestCommentThreadContext(Model):
    """GitPullRequestCommentThreadContext.

    :param change_tracking_id: Used to track a comment across iterations. This value can be found by looking at the iteration's changes list. Must be set for pull requests with iteration support. Otherwise, it's not required for 'legacy' pull requests.
    :type change_tracking_id: int
    :param iteration_context: Specify comparing iteration Ids when a comment thread is added while comparing 2 iterations.
    :type iteration_context: :class:`CommentIterationContext <git.v4_0.models.CommentIterationContext>`
    :param tracking_criteria: The criteria used to track this thread. If this property is filled out when the thread is returned, then the thread has been tracked from its original location using the given criteria.
    :type tracking_criteria: :class:`CommentTrackingCriteria <git.v4_0.models.CommentTrackingCriteria>`
    """

    _attribute_map = {
        'change_tracking_id': {'key': 'changeTrackingId', 'type': 'int'},
        'iteration_context': {'key': 'iterationContext', 'type': 'CommentIterationContext'},
        'tracking_criteria': {'key': 'trackingCriteria', 'type': 'CommentTrackingCriteria'}
    }

    def __init__(self, change_tracking_id=None, iteration_context=None, tracking_criteria=None):
        super(GitPullRequestCommentThreadContext, self).__init__()
        self.change_tracking_id = change_tracking_id
        self.iteration_context = iteration_context
        self.tracking_criteria = tracking_criteria



class GitPullRequestCompletionOptions(Model):
    """GitPullRequestCompletionOptions.

    :param bypass_policy:
    :type bypass_policy: bool
    :param bypass_reason:
    :type bypass_reason: str
    :param delete_source_branch:
    :type delete_source_branch: bool
    :param merge_commit_message:
    :type merge_commit_message: str
    :param squash_merge:
    :type squash_merge: bool
    :param transition_work_items:
    :type transition_work_items: bool
    """

    _attribute_map = {
        'bypass_policy': {'key': 'bypassPolicy', 'type': 'bool'},
        'bypass_reason': {'key': 'bypassReason', 'type': 'str'},
        'delete_source_branch': {'key': 'deleteSourceBranch', 'type': 'bool'},
        'merge_commit_message': {'key': 'mergeCommitMessage', 'type': 'str'},
        'squash_merge': {'key': 'squashMerge', 'type': 'bool'},
        'transition_work_items': {'key': 'transitionWorkItems', 'type': 'bool'}
    }

    def __init__(self, bypass_policy=None, bypass_reason=None, delete_source_branch=None, merge_commit_message=None, squash_merge=None, transition_work_items=None):
        super(GitPullRequestCompletionOptions, self).__init__()
        self.bypass_policy = bypass_policy
        self.bypass_reason = bypass_reason
        self.delete_source_branch = delete_source_branch
        self.merge_commit_message = merge_commit_message
        self.squash_merge = squash_merge
        self.transition_work_items = transition_work_items



class GitPullRequestIteration(Model):
    """GitPullRequestIteration.

    :param _links:
    :type _links: :class:`ReferenceLinks <git.v4_0.models.ReferenceLinks>`
    :param author:
    :type author: :class:`IdentityRef <git.v4_0.models.IdentityRef>`
    :param change_list:
    :type change_list: list of :class:`GitPullRequestChange <git.v4_0.models.GitPullRequestChange>`
    :param commits:
    :type commits: list of :class:`GitCommitRef <git.v4_0.models.GitCommitRef>`
    :param common_ref_commit:
    :type common_ref_commit: :class:`GitCommitRef <git.v4_0.models.GitCommitRef>`
    :param created_date:
    :type created_date: datetime
    :param description:
    :type description: str
    :param has_more_commits:
    :type has_more_commits: bool
    :param id:
    :type id: int
    :param push:
    :type push: :class:`GitPushRef <git.v4_0.models.GitPushRef>`
    :param reason:
    :type reason: object
    :param source_ref_commit:
    :type source_ref_commit: :class:`GitCommitRef <git.v4_0.models.GitCommitRef>`
    :param target_ref_commit:
    :type target_ref_commit: :class:`GitCommitRef <git.v4_0.models.GitCommitRef>`
    :param updated_date:
    :type updated_date: datetime
    """

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'author': {'key': 'author', 'type': 'IdentityRef'},
        'change_list': {'key': 'changeList', 'type': '[GitPullRequestChange]'},
        'commits': {'key': 'commits', 'type': '[GitCommitRef]'},
        'common_ref_commit': {'key': 'commonRefCommit', 'type': 'GitCommitRef'},
        'created_date': {'key': 'createdDate', 'type': 'iso-8601'},
        'description': {'key': 'description', 'type': 'str'},
        'has_more_commits': {'key': 'hasMoreCommits', 'type': 'bool'},
        'id': {'key': 'id', 'type': 'int'},
        'push': {'key': 'push', 'type': 'GitPushRef'},
        'reason': {'key': 'reason', 'type': 'object'},
        'source_ref_commit': {'key': 'sourceRefCommit', 'type': 'GitCommitRef'},
        'target_ref_commit': {'key': 'targetRefCommit', 'type': 'GitCommitRef'},
        'updated_date': {'key': 'updatedDate', 'type': 'iso-8601'}
    }

    def __init__(self, _links=None, author=None, change_list=None, commits=None, common_ref_commit=None, created_date=None, description=None, has_more_commits=None, id=None, push=None, reason=None, source_ref_commit=None, target_ref_commit=None, updated_date=None):
        super(GitPullRequestIteration, self).__init__()
        self._links = _links
        self.author = author
        self.change_list = change_list
        self.commits = commits
        self.common_ref_commit = common_ref_commit
        self.created_date = created_date
        self.description = description
        self.has_more_commits = has_more_commits
        self.id = id
        self.push = push
        self.reason = reason
        self.source_ref_commit = source_ref_commit
        self.target_ref_commit = target_ref_commit
        self.updated_date = updated_date



class GitPullRequestIterationChanges(Model):
    """GitPullRequestIterationChanges.

    :param change_entries:
    :type change_entries: list of :class:`GitPullRequestChange <git.v4_0.models.GitPullRequestChange>`
    :param next_skip:
    :type next_skip: int
    :param next_top:
    :type next_top: int
    """

    _attribute_map = {
        'change_entries': {'key': 'changeEntries', 'type': '[GitPullRequestChange]'},
        'next_skip': {'key': 'nextSkip', 'type': 'int'},
        'next_top': {'key': 'nextTop', 'type': 'int'}
    }

    def __init__(self, change_entries=None, next_skip=None, next_top=None):
        super(GitPullRequestIterationChanges, self).__init__()
        self.change_entries = change_entries
        self.next_skip = next_skip
        self.next_top = next_top



class GitPullRequestMergeOptions(Model):
    """GitPullRequestMergeOptions.

    :param disable_renames:
    :type disable_renames: bool
    """

    _attribute_map = {
        'disable_renames': {'key': 'disableRenames', 'type': 'bool'}
    }

    def __init__(self, disable_renames=None):
        super(GitPullRequestMergeOptions, self).__init__()
        self.disable_renames = disable_renames



class GitPullRequestQuery(Model):
    """GitPullRequestQuery.

    :param queries: The query to perform
    :type queries: list of :class:`GitPullRequestQueryInput <git.v4_0.models.GitPullRequestQueryInput>`
    :param results: The results of the query
    :type results: list of {[GitPullRequest]}
    """

    _attribute_map = {
        'queries': {'key': 'queries', 'type': '[GitPullRequestQueryInput]'},
        'results': {'key': 'results', 'type': '[{[GitPullRequest]}]'}
    }

    def __init__(self, queries=None, results=None):
        super(GitPullRequestQuery, self).__init__()
        self.queries = queries
        self.results = results



class GitPullRequestQueryInput(Model):
    """GitPullRequestQueryInput.

    :param items: The list commit ids to search for.
    :type items: list of str
    :param type: The type of query to perform
    :type type: object
    """

    _attribute_map = {
        'items': {'key': 'items', 'type': '[str]'},
        'type': {'key': 'type', 'type': 'object'}
    }

    def __init__(self, items=None, type=None):
        super(GitPullRequestQueryInput, self).__init__()
        self.items = items
        self.type = type



class GitPullRequestSearchCriteria(Model):
    """GitPullRequestSearchCriteria.

    :param creator_id:
    :type creator_id: str
    :param include_links: Whether to include the _links field on the shallow references
    :type include_links: bool
    :param repository_id:
    :type repository_id: str
    :param reviewer_id:
    :type reviewer_id: str
    :param source_ref_name:
    :type source_ref_name: str
    :param source_repository_id:
    :type source_repository_id: str
    :param status:
    :type status: object
    :param target_ref_name:
    :type target_ref_name: str
    """

    _attribute_map = {
        'creator_id': {'key': 'creatorId', 'type': 'str'},
        'include_links': {'key': 'includeLinks', 'type': 'bool'},
        'repository_id': {'key': 'repositoryId', 'type': 'str'},
        'reviewer_id': {'key': 'reviewerId', 'type': 'str'},
        'source_ref_name': {'key': 'sourceRefName', 'type': 'str'},
        'source_repository_id': {'key': 'sourceRepositoryId', 'type': 'str'},
        'status': {'key': 'status', 'type': 'object'},
        'target_ref_name': {'key': 'targetRefName', 'type': 'str'}
    }

    def __init__(self, creator_id=None, include_links=None, repository_id=None, reviewer_id=None, source_ref_name=None, source_repository_id=None, status=None, target_ref_name=None):
        super(GitPullRequestSearchCriteria, self).__init__()
        self.creator_id = creator_id
        self.include_links = include_links
        self.repository_id = repository_id
        self.reviewer_id = reviewer_id
        self.source_ref_name = source_ref_name
        self.source_repository_id = source_repository_id
        self.status = status
        self.target_ref_name = target_ref_name



class GitPushRef(Model):
    """GitPushRef.

    :param _links:
    :type _links: :class:`ReferenceLinks <git.v4_0.models.ReferenceLinks>`
    :param date:
    :type date: datetime
    :param push_correlation_id:
    :type push_correlation_id: str
    :param pushed_by:
    :type pushed_by: :class:`IdentityRef <git.v4_0.models.IdentityRef>`
    :param push_id:
    :type push_id: int
    :param url:
    :type url: str
    """

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'date': {'key': 'date', 'type': 'iso-8601'},
        'push_correlation_id': {'key': 'pushCorrelationId', 'type': 'str'},
        'pushed_by': {'key': 'pushedBy', 'type': 'IdentityRef'},
        'push_id': {'key': 'pushId', 'type': 'int'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, _links=None, date=None, push_correlation_id=None, pushed_by=None, push_id=None, url=None):
        super(GitPushRef, self).__init__()
        self._links = _links
        self.date = date
        self.push_correlation_id = push_correlation_id
        self.pushed_by = pushed_by
        self.push_id = push_id
        self.url = url



class GitPushSearchCriteria(Model):
    """GitPushSearchCriteria.

    :param from_date:
    :type from_date: datetime
    :param include_links: Whether to include the _links field on the shallow references
    :type include_links: bool
    :param include_ref_updates:
    :type include_ref_updates: bool
    :param pusher_id:
    :type pusher_id: str
    :param ref_name:
    :type ref_name: str
    :param to_date:
    :type to_date: datetime
    """

    _attribute_map = {
        'from_date': {'key': 'fromDate', 'type': 'iso-8601'},
        'include_links': {'key': 'includeLinks', 'type': 'bool'},
        'include_ref_updates': {'key': 'includeRefUpdates', 'type': 'bool'},
        'pusher_id': {'key': 'pusherId', 'type': 'str'},
        'ref_name': {'key': 'refName', 'type': 'str'},
        'to_date': {'key': 'toDate', 'type': 'iso-8601'}
    }

    def __init__(self, from_date=None, include_links=None, include_ref_updates=None, pusher_id=None, ref_name=None, to_date=None):
        super(GitPushSearchCriteria, self).__init__()
        self.from_date = from_date
        self.include_links = include_links
        self.include_ref_updates = include_ref_updates
        self.pusher_id = pusher_id
        self.ref_name = ref_name
        self.to_date = to_date



class GitQueryBranchStatsCriteria(Model):
    """GitQueryBranchStatsCriteria.

    :param base_commit:
    :type base_commit: :class:`GitVersionDescriptor <git.v4_0.models.GitVersionDescriptor>`
    :param target_commits:
    :type target_commits: list of :class:`GitVersionDescriptor <git.v4_0.models.GitVersionDescriptor>`
    """

    _attribute_map = {
        'base_commit': {'key': 'baseCommit', 'type': 'GitVersionDescriptor'},
        'target_commits': {'key': 'targetCommits', 'type': '[GitVersionDescriptor]'}
    }

    def __init__(self, base_commit=None, target_commits=None):
        super(GitQueryBranchStatsCriteria, self).__init__()
        self.base_commit = base_commit
        self.target_commits = target_commits



class GitQueryCommitsCriteria(Model):
    """GitQueryCommitsCriteria.

    :param skip: Number of entries to skip
    :type skip: int
    :param top: Maximum number of entries to retrieve
    :type top: int
    :param author: Alias or display name of the author
    :type author: str
    :param compare_version: If provided, the earliest commit in the graph to search
    :type compare_version: :class:`GitVersionDescriptor <git.v4_0.models.GitVersionDescriptor>`
    :param exclude_deletes: If true, don't include delete history entries
    :type exclude_deletes: bool
    :param from_commit_id: If provided, a lower bound for filtering commits alphabetically
    :type from_commit_id: str
    :param from_date: If provided, only include history entries created after this date (string)
    :type from_date: str
    :param history_mode: What Git history mode should be used. This only applies to the search criteria when Ids = null.
    :type history_mode: object
    :param ids: If provided, specifies the exact commit ids of the commits to fetch. May not be combined with other parameters.
    :type ids: list of str
    :param include_links: Whether to include the _links field on the shallow references
    :type include_links: bool
    :param include_work_items: Whether to include linked work items
    :type include_work_items: bool
    :param item_path: Path of item to search under
    :type item_path: str
    :param item_version: If provided, identifies the commit or branch to search
    :type item_version: :class:`GitVersionDescriptor <git.v4_0.models.GitVersionDescriptor>`
    :param to_commit_id: If provided, an upper bound for filtering commits alphabetically
    :type to_commit_id: str
    :param to_date: If provided, only include history entries created before this date (string)
    :type to_date: str
    :param user: Alias or display name of the committer
    :type user: str
    """

    _attribute_map = {
        'skip': {'key': '$skip', 'type': 'int'},
        'top': {'key': '$top', 'type': 'int'},
        'author': {'key': 'author', 'type': 'str'},
        'compare_version': {'key': 'compareVersion', 'type': 'GitVersionDescriptor'},
        'exclude_deletes': {'key': 'excludeDeletes', 'type': 'bool'},
        'from_commit_id': {'key': 'fromCommitId', 'type': 'str'},
        'from_date': {'key': 'fromDate', 'type': 'str'},
        'history_mode': {'key': 'historyMode', 'type': 'object'},
        'ids': {'key': 'ids', 'type': '[str]'},
        'include_links': {'key': 'includeLinks', 'type': 'bool'},
        'include_work_items': {'key': 'includeWorkItems', 'type': 'bool'},
        'item_path': {'key': 'itemPath', 'type': 'str'},
        'item_version': {'key': 'itemVersion', 'type': 'GitVersionDescriptor'},
        'to_commit_id': {'key': 'toCommitId', 'type': 'str'},
        'to_date': {'key': 'toDate', 'type': 'str'},
        'user': {'key': 'user', 'type': 'str'}
    }

    def __init__(self, skip=None, top=None, author=None, compare_version=None, exclude_deletes=None, from_commit_id=None, from_date=None, history_mode=None, ids=None, include_links=None, include_work_items=None, item_path=None, item_version=None, to_commit_id=None, to_date=None, user=None):
        super(GitQueryCommitsCriteria, self).__init__()
        self.skip = skip
        self.top = top
        self.author = author
        self.compare_version = compare_version
        self.exclude_deletes = exclude_deletes
        self.from_commit_id = from_commit_id
        self.from_date = from_date
        self.history_mode = history_mode
        self.ids = ids
        self.include_links = include_links
        self.include_work_items = include_work_items
        self.item_path = item_path
        self.item_version = item_version
        self.to_commit_id = to_commit_id
        self.to_date = to_date
        self.user = user



class GitRef(Model):
    """GitRef.

    :param _links:
    :type _links: :class:`ReferenceLinks <git.v4_0.models.ReferenceLinks>`
    :param is_locked:
    :type is_locked: bool
    :param is_locked_by:
    :type is_locked_by: :class:`IdentityRef <git.v4_0.models.IdentityRef>`
    :param name:
    :type name: str
    :param object_id:
    :type object_id: str
    :param peeled_object_id:
    :type peeled_object_id: str
    :param statuses:
    :type statuses: list of :class:`GitStatus <git.v4_0.models.GitStatus>`
    :param url:
    :type url: str
    """

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'is_locked': {'key': 'isLocked', 'type': 'bool'},
        'is_locked_by': {'key': 'isLockedBy', 'type': 'IdentityRef'},
        'name': {'key': 'name', 'type': 'str'},
        'object_id': {'key': 'objectId', 'type': 'str'},
        'peeled_object_id': {'key': 'peeledObjectId', 'type': 'str'},
        'statuses': {'key': 'statuses', 'type': '[GitStatus]'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, _links=None, is_locked=None, is_locked_by=None, name=None, object_id=None, peeled_object_id=None, statuses=None, url=None):
        super(GitRef, self).__init__()
        self._links = _links
        self.is_locked = is_locked
        self.is_locked_by = is_locked_by
        self.name = name
        self.object_id = object_id
        self.peeled_object_id = peeled_object_id
        self.statuses = statuses
        self.url = url



class GitRefFavorite(Model):
    """GitRefFavorite.

    :param _links:
    :type _links: :class:`ReferenceLinks <git.v4_0.models.ReferenceLinks>`
    :param id:
    :type id: int
    :param identity_id:
    :type identity_id: str
    :param name:
    :type name: str
    :param repository_id:
    :type repository_id: str
    :param type:
    :type type: object
    :param url:
    :type url: str
    """

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'id': {'key': 'id', 'type': 'int'},
        'identity_id': {'key': 'identityId', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'repository_id': {'key': 'repositoryId', 'type': 'str'},
        'type': {'key': 'type', 'type': 'object'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, _links=None, id=None, identity_id=None, name=None, repository_id=None, type=None, url=None):
        super(GitRefFavorite, self).__init__()
        self._links = _links
        self.id = id
        self.identity_id = identity_id
        self.name = name
        self.repository_id = repository_id
        self.type = type
        self.url = url



class GitRefUpdate(Model):
    """GitRefUpdate.

    :param is_locked:
    :type is_locked: bool
    :param name:
    :type name: str
    :param new_object_id:
    :type new_object_id: str
    :param old_object_id:
    :type old_object_id: str
    :param repository_id:
    :type repository_id: str
    """

    _attribute_map = {
        'is_locked': {'key': 'isLocked', 'type': 'bool'},
        'name': {'key': 'name', 'type': 'str'},
        'new_object_id': {'key': 'newObjectId', 'type': 'str'},
        'old_object_id': {'key': 'oldObjectId', 'type': 'str'},
        'repository_id': {'key': 'repositoryId', 'type': 'str'}
    }

    def __init__(self, is_locked=None, name=None, new_object_id=None, old_object_id=None, repository_id=None):
        super(GitRefUpdate, self).__init__()
        self.is_locked = is_locked
        self.name = name
        self.new_object_id = new_object_id
        self.old_object_id = old_object_id
        self.repository_id = repository_id



class GitRefUpdateResult(Model):
    """GitRefUpdateResult.

    :param custom_message: Custom message for the result object For instance, Reason for failing.
    :type custom_message: str
    :param is_locked: Whether the ref is locked or not
    :type is_locked: bool
    :param name: Ref name
    :type name: str
    :param new_object_id: New object ID
    :type new_object_id: str
    :param old_object_id: Old object ID
    :type old_object_id: str
    :param rejected_by: Name of the plugin that rejected the updated.
    :type rejected_by: str
    :param repository_id: Repository ID
    :type repository_id: str
    :param success: True if the ref update succeeded, false otherwise
    :type success: bool
    :param update_status: Status of the update from the TFS server.
    :type update_status: object
    """

    _attribute_map = {
        'custom_message': {'key': 'customMessage', 'type': 'str'},
        'is_locked': {'key': 'isLocked', 'type': 'bool'},
        'name': {'key': 'name', 'type': 'str'},
        'new_object_id': {'key': 'newObjectId', 'type': 'str'},
        'old_object_id': {'key': 'oldObjectId', 'type': 'str'},
        'rejected_by': {'key': 'rejectedBy', 'type': 'str'},
        'repository_id': {'key': 'repositoryId', 'type': 'str'},
        'success': {'key': 'success', 'type': 'bool'},
        'update_status': {'key': 'updateStatus', 'type': 'object'}
    }

    def __init__(self, custom_message=None, is_locked=None, name=None, new_object_id=None, old_object_id=None, rejected_by=None, repository_id=None, success=None, update_status=None):
        super(GitRefUpdateResult, self).__init__()
        self.custom_message = custom_message
        self.is_locked = is_locked
        self.name = name
        self.new_object_id = new_object_id
        self.old_object_id = old_object_id
        self.rejected_by = rejected_by
        self.repository_id = repository_id
        self.success = success
        self.update_status = update_status



class GitRepository(Model):
    """GitRepository.

    :param _links:
    :type _links: :class:`ReferenceLinks <git.v4_0.models.ReferenceLinks>`
    :param default_branch:
    :type default_branch: str
    :param id:
    :type id: str
    :param is_fork: True if the repository was created as a fork
    :type is_fork: bool
    :param name:
    :type name: str
    :param parent_repository:
    :type parent_repository: :class:`GitRepositoryRef <git.v4_0.models.GitRepositoryRef>`
    :param project:
    :type project: :class:`TeamProjectReference <git.v4_0.models.TeamProjectReference>`
    :param remote_url:
    :type remote_url: str
    :param url:
    :type url: str
    :param valid_remote_urls:
    :type valid_remote_urls: list of str
    """

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'default_branch': {'key': 'defaultBranch', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'is_fork': {'key': 'isFork', 'type': 'bool'},
        'name': {'key': 'name', 'type': 'str'},
        'parent_repository': {'key': 'parentRepository', 'type': 'GitRepositoryRef'},
        'project': {'key': 'project', 'type': 'TeamProjectReference'},
        'remote_url': {'key': 'remoteUrl', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'},
        'valid_remote_urls': {'key': 'validRemoteUrls', 'type': '[str]'}
    }

    def __init__(self, _links=None, default_branch=None, id=None, is_fork=None, name=None, parent_repository=None, project=None, remote_url=None, url=None, valid_remote_urls=None):
        super(GitRepository, self).__init__()
        self._links = _links
        self.default_branch = default_branch
        self.id = id
        self.is_fork = is_fork
        self.name = name
        self.parent_repository = parent_repository
        self.project = project
        self.remote_url = remote_url
        self.url = url
        self.valid_remote_urls = valid_remote_urls



class GitRepositoryCreateOptions(Model):
    """GitRepositoryCreateOptions.

    :param name:
    :type name: str
    :param parent_repository:
    :type parent_repository: :class:`GitRepositoryRef <git.v4_0.models.GitRepositoryRef>`
    :param project:
    :type project: :class:`TeamProjectReference <git.v4_0.models.TeamProjectReference>`
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'parent_repository': {'key': 'parentRepository', 'type': 'GitRepositoryRef'},
        'project': {'key': 'project', 'type': 'TeamProjectReference'}
    }

    def __init__(self, name=None, parent_repository=None, project=None):
        super(GitRepositoryCreateOptions, self).__init__()
        self.name = name
        self.parent_repository = parent_repository
        self.project = project



class GitRepositoryRef(Model):
    """GitRepositoryRef.

    :param collection: Team Project Collection where this Fork resides
    :type collection: :class:`TeamProjectCollectionReference <git.v4_0.models.TeamProjectCollectionReference>`
    :param id:
    :type id: str
    :param name:
    :type name: str
    :param project:
    :type project: :class:`TeamProjectReference <git.v4_0.models.TeamProjectReference>`
    :param remote_url:
    :type remote_url: str
    :param url:
    :type url: str
    """

    _attribute_map = {
        'collection': {'key': 'collection', 'type': 'TeamProjectCollectionReference'},
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'project': {'key': 'project', 'type': 'TeamProjectReference'},
        'remote_url': {'key': 'remoteUrl', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, collection=None, id=None, name=None, project=None, remote_url=None, url=None):
        super(GitRepositoryRef, self).__init__()
        self.collection = collection
        self.id = id
        self.name = name
        self.project = project
        self.remote_url = remote_url
        self.url = url



class GitRepositoryStats(Model):
    """GitRepositoryStats.

    :param active_pull_requests_count:
    :type active_pull_requests_count: int
    :param branches_count:
    :type branches_count: int
    :param commits_count:
    :type commits_count: int
    :param repository_id:
    :type repository_id: str
    """

    _attribute_map = {
        'active_pull_requests_count': {'key': 'activePullRequestsCount', 'type': 'int'},
        'branches_count': {'key': 'branchesCount', 'type': 'int'},
        'commits_count': {'key': 'commitsCount', 'type': 'int'},
        'repository_id': {'key': 'repositoryId', 'type': 'str'}
    }

    def __init__(self, active_pull_requests_count=None, branches_count=None, commits_count=None, repository_id=None):
        super(GitRepositoryStats, self).__init__()
        self.active_pull_requests_count = active_pull_requests_count
        self.branches_count = branches_count
        self.commits_count = commits_count
        self.repository_id = repository_id



class GitRevert(GitAsyncRefOperation):
    """GitRevert.

    :param _links:
    :type _links: :class:`ReferenceLinks <git.v4_0.models.ReferenceLinks>`
    :param detailed_status:
    :type detailed_status: :class:`GitAsyncRefOperationDetail <git.v4_0.models.GitAsyncRefOperationDetail>`
    :param parameters:
    :type parameters: :class:`GitAsyncRefOperationParameters <git.v4_0.models.GitAsyncRefOperationParameters>`
    :param status:
    :type status: object
    :param url:
    :type url: str
    :param revert_id:
    :type revert_id: int
    """

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'detailed_status': {'key': 'detailedStatus', 'type': 'GitAsyncRefOperationDetail'},
        'parameters': {'key': 'parameters', 'type': 'GitAsyncRefOperationParameters'},
        'status': {'key': 'status', 'type': 'object'},
        'url': {'key': 'url', 'type': 'str'},
        'revert_id': {'key': 'revertId', 'type': 'int'}
    }

    def __init__(self, _links=None, detailed_status=None, parameters=None, status=None, url=None, revert_id=None):
        super(GitRevert, self).__init__(_links=_links, detailed_status=detailed_status, parameters=parameters, status=status, url=url)
        self.revert_id = revert_id



class GitStatus(Model):
    """GitStatus.

    :param _links: Reference links.
    :type _links: :class:`ReferenceLinks <git.v4_0.models.ReferenceLinks>`
    :param context: Context of the status.
    :type context: :class:`GitStatusContext <git.v4_0.models.GitStatusContext>`
    :param created_by: Identity that created the status.
    :type created_by: :class:`IdentityRef <git.v4_0.models.IdentityRef>`
    :param creation_date: Creation date and time of the status.
    :type creation_date: datetime
    :param description: Status description. Typically describes current state of the status.
    :type description: str
    :param id: Status identifier.
    :type id: int
    :param state: State of the status.
    :type state: object
    :param target_url: URL with status details.
    :type target_url: str
    :param updated_date: Last update date and time of the status.
    :type updated_date: datetime
    """

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'context': {'key': 'context', 'type': 'GitStatusContext'},
        'created_by': {'key': 'createdBy', 'type': 'IdentityRef'},
        'creation_date': {'key': 'creationDate', 'type': 'iso-8601'},
        'description': {'key': 'description', 'type': 'str'},
        'id': {'key': 'id', 'type': 'int'},
        'state': {'key': 'state', 'type': 'object'},
        'target_url': {'key': 'targetUrl', 'type': 'str'},
        'updated_date': {'key': 'updatedDate', 'type': 'iso-8601'}
    }

    def __init__(self, _links=None, context=None, created_by=None, creation_date=None, description=None, id=None, state=None, target_url=None, updated_date=None):
        super(GitStatus, self).__init__()
        self._links = _links
        self.context = context
        self.created_by = created_by
        self.creation_date = creation_date
        self.description = description
        self.id = id
        self.state = state
        self.target_url = target_url
        self.updated_date = updated_date



class GitStatusContext(Model):
    """GitStatusContext.

    :param genre: Genre of the status. Typically name of the service/tool generating the status, can be empty.
    :type genre: str
    :param name: Name identifier of the status, cannot be null or empty.
    :type name: str
    """

    _attribute_map = {
        'genre': {'key': 'genre', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'}
    }

    def __init__(self, genre=None, name=None):
        super(GitStatusContext, self).__init__()
        self.genre = genre
        self.name = name



class GitSuggestion(Model):
    """GitSuggestion.

    :param properties:
    :type properties: dict
    :param type:
    :type type: str
    """

    _attribute_map = {
        'properties': {'key': 'properties', 'type': '{object}'},
        'type': {'key': 'type', 'type': 'str'}
    }

    def __init__(self, properties=None, type=None):
        super(GitSuggestion, self).__init__()
        self.properties = properties
        self.type = type



class GitTemplate(Model):
    """GitTemplate.

    :param name: Name of the Template
    :type name: str
    :param type: Type of the Template
    :type type: str
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'}
    }

    def __init__(self, name=None, type=None):
        super(GitTemplate, self).__init__()
        self.name = name
        self.type = type



class GitTreeDiff(Model):
    """GitTreeDiff.

    :param base_tree_id: ObjectId of the base tree of this diff.
    :type base_tree_id: str
    :param diff_entries: List of tree entries that differ between the base and target tree.  Renames and object type changes are returned as a delete for the old object and add for the new object.  If a continuation token is returned in the response header, some tree entries are yet to be processed and may yeild more diff entries. If the continuation token is not returned all the diff entries have been included in this response.
    :type diff_entries: list of :class:`GitTreeDiffEntry <git.v4_0.models.GitTreeDiffEntry>`
    :param target_tree_id: ObjectId of the target tree of this diff.
    :type target_tree_id: str
    :param url: REST Url to this resource.
    :type url: str
    """

    _attribute_map = {
        'base_tree_id': {'key': 'baseTreeId', 'type': 'str'},
        'diff_entries': {'key': 'diffEntries', 'type': '[GitTreeDiffEntry]'},
        'target_tree_id': {'key': 'targetTreeId', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, base_tree_id=None, diff_entries=None, target_tree_id=None, url=None):
        super(GitTreeDiff, self).__init__()
        self.base_tree_id = base_tree_id
        self.diff_entries = diff_entries
        self.target_tree_id = target_tree_id
        self.url = url



class GitTreeDiffEntry(Model):
    """GitTreeDiffEntry.

    :param base_object_id: SHA1 hash of the object in the base tree, if it exists. Will be null in case of adds.
    :type base_object_id: str
    :param change_type: Type of change that affected this entry.
    :type change_type: object
    :param object_type: Object type of the tree entry. Blob, Tree or Commit("submodule")
    :type object_type: object
    :param path: Relative path in base and target trees.
    :type path: str
    :param target_object_id: SHA1 hash of the object in the target tree, if it exists. Will be null in case of deletes.
    :type target_object_id: str
    """

    _attribute_map = {
        'base_object_id': {'key': 'baseObjectId', 'type': 'str'},
        'change_type': {'key': 'changeType', 'type': 'object'},
        'object_type': {'key': 'objectType', 'type': 'object'},
        'path': {'key': 'path', 'type': 'str'},
        'target_object_id': {'key': 'targetObjectId', 'type': 'str'}
    }

    def __init__(self, base_object_id=None, change_type=None, object_type=None, path=None, target_object_id=None):
        super(GitTreeDiffEntry, self).__init__()
        self.base_object_id = base_object_id
        self.change_type = change_type
        self.object_type = object_type
        self.path = path
        self.target_object_id = target_object_id



class GitTreeDiffResponse(Model):
    """GitTreeDiffResponse.

    :param continuation_token: The HTTP client methods find the continuation token header in the response and populate this field.
    :type continuation_token: list of str
    :param tree_diff:
    :type tree_diff: :class:`GitTreeDiff <git.v4_0.models.GitTreeDiff>`
    """

    _attribute_map = {
        'continuation_token': {'key': 'continuationToken', 'type': '[str]'},
        'tree_diff': {'key': 'treeDiff', 'type': 'GitTreeDiff'}
    }

    def __init__(self, continuation_token=None, tree_diff=None):
        super(GitTreeDiffResponse, self).__init__()
        self.continuation_token = continuation_token
        self.tree_diff = tree_diff



class GitTreeEntryRef(Model):
    """GitTreeEntryRef.

    :param git_object_type: Blob or tree
    :type git_object_type: object
    :param mode: Mode represented as octal string
    :type mode: str
    :param object_id: SHA1 hash of git object
    :type object_id: str
    :param relative_path: Path relative to parent tree object
    :type relative_path: str
    :param size: Size of content
    :type size: long
    :param url: url to retrieve tree or blob
    :type url: str
    """

    _attribute_map = {
        'git_object_type': {'key': 'gitObjectType', 'type': 'object'},
        'mode': {'key': 'mode', 'type': 'str'},
        'object_id': {'key': 'objectId', 'type': 'str'},
        'relative_path': {'key': 'relativePath', 'type': 'str'},
        'size': {'key': 'size', 'type': 'long'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, git_object_type=None, mode=None, object_id=None, relative_path=None, size=None, url=None):
        super(GitTreeEntryRef, self).__init__()
        self.git_object_type = git_object_type
        self.mode = mode
        self.object_id = object_id
        self.relative_path = relative_path
        self.size = size
        self.url = url



class GitTreeRef(Model):
    """GitTreeRef.

    :param _links:
    :type _links: :class:`ReferenceLinks <git.v4_0.models.ReferenceLinks>`
    :param object_id: SHA1 hash of git object
    :type object_id: str
    :param size: Sum of sizes of all children
    :type size: long
    :param tree_entries: Blobs and trees under this tree
    :type tree_entries: list of :class:`GitTreeEntryRef <git.v4_0.models.GitTreeEntryRef>`
    :param url: Url to tree
    :type url: str
    """

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'object_id': {'key': 'objectId', 'type': 'str'},
        'size': {'key': 'size', 'type': 'long'},
        'tree_entries': {'key': 'treeEntries', 'type': '[GitTreeEntryRef]'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, _links=None, object_id=None, size=None, tree_entries=None, url=None):
        super(GitTreeRef, self).__init__()
        self._links = _links
        self.object_id = object_id
        self.size = size
        self.tree_entries = tree_entries
        self.url = url



class GitUserDate(Model):
    """GitUserDate.

    :param date:
    :type date: datetime
    :param email:
    :type email: str
    :param name:
    :type name: str
    """

    _attribute_map = {
        'date': {'key': 'date', 'type': 'iso-8601'},
        'email': {'key': 'email', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'}
    }

    def __init__(self, date=None, email=None, name=None):
        super(GitUserDate, self).__init__()
        self.date = date
        self.email = email
        self.name = name



class GitVersionDescriptor(Model):
    """GitVersionDescriptor.

    :param version: Version string identifier (name of tag/branch, SHA1 of commit)
    :type version: str
    :param version_options: Version options - Specify additional modifiers to version (e.g Previous)
    :type version_options: object
    :param version_type: Version type (branch, tag, or commit). Determines how Id is interpreted
    :type version_type: object
    """

    _attribute_map = {
        'version': {'key': 'version', 'type': 'str'},
        'version_options': {'key': 'versionOptions', 'type': 'object'},
        'version_type': {'key': 'versionType', 'type': 'object'}
    }

    def __init__(self, version=None, version_options=None, version_type=None):
        super(GitVersionDescriptor, self).__init__()
        self.version = version
        self.version_options = version_options
        self.version_type = version_type



class GlobalGitRepositoryKey(Model):
    """GlobalGitRepositoryKey.

    :param collection_id:
    :type collection_id: str
    :param project_id:
    :type project_id: str
    :param repository_id:
    :type repository_id: str
    """

    _attribute_map = {
        'collection_id': {'key': 'collectionId', 'type': 'str'},
        'project_id': {'key': 'projectId', 'type': 'str'},
        'repository_id': {'key': 'repositoryId', 'type': 'str'}
    }

    def __init__(self, collection_id=None, project_id=None, repository_id=None):
        super(GlobalGitRepositoryKey, self).__init__()
        self.collection_id = collection_id
        self.project_id = project_id
        self.repository_id = repository_id



class IdentityRef(Model):
    """IdentityRef.

    :param directory_alias:
    :type directory_alias: str
    :param display_name:
    :type display_name: str
    :param id:
    :type id: str
    :param image_url:
    :type image_url: str
    :param inactive:
    :type inactive: bool
    :param is_aad_identity:
    :type is_aad_identity: bool
    :param is_container:
    :type is_container: bool
    :param profile_url:
    :type profile_url: str
    :param unique_name:
    :type unique_name: str
    :param url:
    :type url: str
    """

    _attribute_map = {
        'directory_alias': {'key': 'directoryAlias', 'type': 'str'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'image_url': {'key': 'imageUrl', 'type': 'str'},
        'inactive': {'key': 'inactive', 'type': 'bool'},
        'is_aad_identity': {'key': 'isAadIdentity', 'type': 'bool'},
        'is_container': {'key': 'isContainer', 'type': 'bool'},
        'profile_url': {'key': 'profileUrl', 'type': 'str'},
        'unique_name': {'key': 'uniqueName', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, directory_alias=None, display_name=None, id=None, image_url=None, inactive=None, is_aad_identity=None, is_container=None, profile_url=None, unique_name=None, url=None):
        super(IdentityRef, self).__init__()
        self.directory_alias = directory_alias
        self.display_name = display_name
        self.id = id
        self.image_url = image_url
        self.inactive = inactive
        self.is_aad_identity = is_aad_identity
        self.is_container = is_container
        self.profile_url = profile_url
        self.unique_name = unique_name
        self.url = url



class IdentityRefWithVote(IdentityRef):
    """IdentityRefWithVote.

    :param directory_alias:
    :type directory_alias: str
    :param display_name:
    :type display_name: str
    :param id:
    :type id: str
    :param image_url:
    :type image_url: str
    :param inactive:
    :type inactive: bool
    :param is_aad_identity:
    :type is_aad_identity: bool
    :param is_container:
    :type is_container: bool
    :param profile_url:
    :type profile_url: str
    :param unique_name:
    :type unique_name: str
    :param url:
    :type url: str
    :param is_required:
    :type is_required: bool
    :param reviewer_url:
    :type reviewer_url: str
    :param vote:
    :type vote: int
    :param voted_for:
    :type voted_for: list of :class:`IdentityRefWithVote <git.v4_0.models.IdentityRefWithVote>`
    """

    _attribute_map = {
        'directory_alias': {'key': 'directoryAlias', 'type': 'str'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'image_url': {'key': 'imageUrl', 'type': 'str'},
        'inactive': {'key': 'inactive', 'type': 'bool'},
        'is_aad_identity': {'key': 'isAadIdentity', 'type': 'bool'},
        'is_container': {'key': 'isContainer', 'type': 'bool'},
        'profile_url': {'key': 'profileUrl', 'type': 'str'},
        'unique_name': {'key': 'uniqueName', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'},
        'is_required': {'key': 'isRequired', 'type': 'bool'},
        'reviewer_url': {'key': 'reviewerUrl', 'type': 'str'},
        'vote': {'key': 'vote', 'type': 'int'},
        'voted_for': {'key': 'votedFor', 'type': '[IdentityRefWithVote]'}
    }

    def __init__(self, directory_alias=None, display_name=None, id=None, image_url=None, inactive=None, is_aad_identity=None, is_container=None, profile_url=None, unique_name=None, url=None, is_required=None, reviewer_url=None, vote=None, voted_for=None):
        super(IdentityRefWithVote, self).__init__(directory_alias=directory_alias, display_name=display_name, id=id, image_url=image_url, inactive=inactive, is_aad_identity=is_aad_identity, is_container=is_container, profile_url=profile_url, unique_name=unique_name, url=url)
        self.is_required = is_required
        self.reviewer_url = reviewer_url
        self.vote = vote
        self.voted_for = voted_for



class ImportRepositoryValidation(Model):
    """ImportRepositoryValidation.

    :param git_source:
    :type git_source: :class:`GitImportGitSource <git.v4_0.models.GitImportGitSource>`
    :param password:
    :type password: str
    :param tfvc_source:
    :type tfvc_source: :class:`GitImportTfvcSource <git.v4_0.models.GitImportTfvcSource>`
    :param username:
    :type username: str
    """

    _attribute_map = {
        'git_source': {'key': 'gitSource', 'type': 'GitImportGitSource'},
        'password': {'key': 'password', 'type': 'str'},
        'tfvc_source': {'key': 'tfvcSource', 'type': 'GitImportTfvcSource'},
        'username': {'key': 'username', 'type': 'str'}
    }

    def __init__(self, git_source=None, password=None, tfvc_source=None, username=None):
        super(ImportRepositoryValidation, self).__init__()
        self.git_source = git_source
        self.password = password
        self.tfvc_source = tfvc_source
        self.username = username



class ItemContent(Model):
    """ItemContent.

    :param content:
    :type content: str
    :param content_type:
    :type content_type: object
    """

    _attribute_map = {
        'content': {'key': 'content', 'type': 'str'},
        'content_type': {'key': 'contentType', 'type': 'object'}
    }

    def __init__(self, content=None, content_type=None):
        super(ItemContent, self).__init__()
        self.content = content
        self.content_type = content_type



class ItemModel(Model):
    """ItemModel.

    :param _links:
    :type _links: :class:`ReferenceLinks <git.v4_0.models.ReferenceLinks>`
    :param content_metadata:
    :type content_metadata: :class:`FileContentMetadata <git.v4_0.models.FileContentMetadata>`
    :param is_folder:
    :type is_folder: bool
    :param is_sym_link:
    :type is_sym_link: bool
    :param path:
    :type path: str
    :param url:
    :type url: str
    """

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'content_metadata': {'key': 'contentMetadata', 'type': 'FileContentMetadata'},
        'is_folder': {'key': 'isFolder', 'type': 'bool'},
        'is_sym_link': {'key': 'isSymLink', 'type': 'bool'},
        'path': {'key': 'path', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, _links=None, content_metadata=None, is_folder=None, is_sym_link=None, path=None, url=None):
        super(ItemModel, self).__init__()
        self._links = _links
        self.content_metadata = content_metadata
        self.is_folder = is_folder
        self.is_sym_link = is_sym_link
        self.path = path
        self.url = url



class ReferenceLinks(Model):
    """ReferenceLinks.

    :param links: The readonly view of the links.  Because Reference links are readonly, we only want to expose them as read only.
    :type links: dict
    """

    _attribute_map = {
        'links': {'key': 'links', 'type': '{object}'}
    }

    def __init__(self, links=None):
        super(ReferenceLinks, self).__init__()
        self.links = links



class ResourceRef(Model):
    """ResourceRef.

    :param id:
    :type id: str
    :param url:
    :type url: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, id=None, url=None):
        super(ResourceRef, self).__init__()
        self.id = id
        self.url = url



class ShareNotificationContext(Model):
    """ShareNotificationContext.

    :param message: Optional user note or message.
    :type message: str
    :param receivers: Identities of users who will receive a share notification.
    :type receivers: list of :class:`IdentityRef <git.v4_0.models.IdentityRef>`
    """

    _attribute_map = {
        'message': {'key': 'message', 'type': 'str'},
        'receivers': {'key': 'receivers', 'type': '[IdentityRef]'}
    }

    def __init__(self, message=None, receivers=None):
        super(ShareNotificationContext, self).__init__()
        self.message = message
        self.receivers = receivers



class SourceToTargetRef(Model):
    """SourceToTargetRef.

    :param source_ref: The source ref to copy. For example, refs/heads/master.
    :type source_ref: str
    :param target_ref: The target ref to update. For example, refs/heads/master
    :type target_ref: str
    """

    _attribute_map = {
        'source_ref': {'key': 'sourceRef', 'type': 'str'},
        'target_ref': {'key': 'targetRef', 'type': 'str'}
    }

    def __init__(self, source_ref=None, target_ref=None):
        super(SourceToTargetRef, self).__init__()
        self.source_ref = source_ref
        self.target_ref = target_ref



class TeamProjectCollectionReference(Model):
    """TeamProjectCollectionReference.

    :param id: Collection Id.
    :type id: str
    :param name: Collection Name.
    :type name: str
    :param url: Collection REST Url.
    :type url: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, id=None, name=None, url=None):
        super(TeamProjectCollectionReference, self).__init__()
        self.id = id
        self.name = name
        self.url = url



class TeamProjectReference(Model):
    """TeamProjectReference.

    :param abbreviation: Project abbreviation.
    :type abbreviation: str
    :param description: The project's description (if any).
    :type description: str
    :param id: Project identifier.
    :type id: str
    :param name: Project name.
    :type name: str
    :param revision: Project revision.
    :type revision: long
    :param state: Project state.
    :type state: object
    :param url: Url to the full version of the object.
    :type url: str
    :param visibility: Project visibility.
    :type visibility: object
    """

    _attribute_map = {
        'abbreviation': {'key': 'abbreviation', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'revision': {'key': 'revision', 'type': 'long'},
        'state': {'key': 'state', 'type': 'object'},
        'url': {'key': 'url', 'type': 'str'},
        'visibility': {'key': 'visibility', 'type': 'object'}
    }

    def __init__(self, abbreviation=None, description=None, id=None, name=None, revision=None, state=None, url=None, visibility=None):
        super(TeamProjectReference, self).__init__()
        self.abbreviation = abbreviation
        self.description = description
        self.id = id
        self.name = name
        self.revision = revision
        self.state = state
        self.url = url
        self.visibility = visibility



class VstsInfo(Model):
    """VstsInfo.

    :param collection:
    :type collection: :class:`TeamProjectCollectionReference <git.v4_0.models.TeamProjectCollectionReference>`
    :param repository:
    :type repository: :class:`GitRepository <git.v4_0.models.GitRepository>`
    :param server_url:
    :type server_url: str
    """

    _attribute_map = {
        'collection': {'key': 'collection', 'type': 'TeamProjectCollectionReference'},
        'repository': {'key': 'repository', 'type': 'GitRepository'},
        'server_url': {'key': 'serverUrl', 'type': 'str'}
    }

    def __init__(self, collection=None, repository=None, server_url=None):
        super(VstsInfo, self).__init__()
        self.collection = collection
        self.repository = repository
        self.server_url = server_url



class WebApiCreateTagRequestData(Model):
    """WebApiCreateTagRequestData.

    :param name:
    :type name: str
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'}
    }

    def __init__(self, name=None):
        super(WebApiCreateTagRequestData, self).__init__()
        self.name = name



class WebApiTagDefinition(Model):
    """WebApiTagDefinition.

    :param active:
    :type active: bool
    :param id:
    :type id: str
    :param name:
    :type name: str
    :param url:
    :type url: str
    """

    _attribute_map = {
        'active': {'key': 'active', 'type': 'bool'},
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, active=None, id=None, name=None, url=None):
        super(WebApiTagDefinition, self).__init__()
        self.active = active
        self.id = id
        self.name = name
        self.url = url



class GitBaseVersionDescriptor(GitVersionDescriptor):
    """GitBaseVersionDescriptor.

    :param version: Version string identifier (name of tag/branch, SHA1 of commit)
    :type version: str
    :param version_options: Version options - Specify additional modifiers to version (e.g Previous)
    :type version_options: object
    :param version_type: Version type (branch, tag, or commit). Determines how Id is interpreted
    :type version_type: object
    :param base_version: Version string identifier (name of tag/branch, SHA1 of commit)
    :type base_version: str
    :param base_version_options: Version options - Specify additional modifiers to version (e.g Previous)
    :type base_version_options: object
    :param base_version_type: Version type (branch, tag, or commit). Determines how Id is interpreted
    :type base_version_type: object
    """

    _attribute_map = {
        'version': {'key': 'version', 'type': 'str'},
        'version_options': {'key': 'versionOptions', 'type': 'object'},
        'version_type': {'key': 'versionType', 'type': 'object'},
        'base_version': {'key': 'baseVersion', 'type': 'str'},
        'base_version_options': {'key': 'baseVersionOptions', 'type': 'object'},
        'base_version_type': {'key': 'baseVersionType', 'type': 'object'}
    }

    def __init__(self, version=None, version_options=None, version_type=None, base_version=None, base_version_options=None, base_version_type=None):
        super(GitBaseVersionDescriptor, self).__init__(version=version, version_options=version_options, version_type=version_type)
        self.base_version = base_version
        self.base_version_options = base_version_options
        self.base_version_type = base_version_type



class GitCommit(GitCommitRef):
    """GitCommit.

    :param _links:
    :type _links: :class:`ReferenceLinks <git.v4_0.models.ReferenceLinks>`
    :param author:
    :type author: :class:`GitUserDate <git.v4_0.models.GitUserDate>`
    :param change_counts:
    :type change_counts: dict
    :param changes:
    :type changes: list of :class:`object <git.v4_0.models.object>`
    :param comment:
    :type comment: str
    :param comment_truncated:
    :type comment_truncated: bool
    :param commit_id:
    :type commit_id: str
    :param committer:
    :type committer: :class:`GitUserDate <git.v4_0.models.GitUserDate>`
    :param parents:
    :type parents: list of str
    :param remote_url:
    :type remote_url: str
    :param statuses:
    :type statuses: list of :class:`GitStatus <git.v4_0.models.GitStatus>`
    :param url:
    :type url: str
    :param work_items:
    :type work_items: list of :class:`ResourceRef <git.v4_0.models.ResourceRef>`
    :param push:
    :type push: :class:`GitPushRef <git.v4_0.models.GitPushRef>`
    :param tree_id:
    :type tree_id: str
    """

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'author': {'key': 'author', 'type': 'GitUserDate'},
        'change_counts': {'key': 'changeCounts', 'type': '{int}'},
        'changes': {'key': 'changes', 'type': '[object]'},
        'comment': {'key': 'comment', 'type': 'str'},
        'comment_truncated': {'key': 'commentTruncated', 'type': 'bool'},
        'commit_id': {'key': 'commitId', 'type': 'str'},
        'committer': {'key': 'committer', 'type': 'GitUserDate'},
        'parents': {'key': 'parents', 'type': '[str]'},
        'remote_url': {'key': 'remoteUrl', 'type': 'str'},
        'statuses': {'key': 'statuses', 'type': '[GitStatus]'},
        'url': {'key': 'url', 'type': 'str'},
        'work_items': {'key': 'workItems', 'type': '[ResourceRef]'},
        'push': {'key': 'push', 'type': 'GitPushRef'},
        'tree_id': {'key': 'treeId', 'type': 'str'}
    }

    def __init__(self, _links=None, author=None, change_counts=None, changes=None, comment=None, comment_truncated=None, commit_id=None, committer=None, parents=None, remote_url=None, statuses=None, url=None, work_items=None, push=None, tree_id=None):
        super(GitCommit, self).__init__(_links=_links, author=author, change_counts=change_counts, changes=changes, comment=comment, comment_truncated=comment_truncated, commit_id=commit_id, committer=committer, parents=parents, remote_url=remote_url, statuses=statuses, url=url, work_items=work_items)
        self.push = push
        self.tree_id = tree_id



class GitForkRef(GitRef):
    """GitForkRef.

    :param _links:
    :type _links: :class:`ReferenceLinks <git.v4_0.models.ReferenceLinks>`
    :param is_locked:
    :type is_locked: bool
    :param is_locked_by:
    :type is_locked_by: :class:`IdentityRef <git.v4_0.models.IdentityRef>`
    :param name:
    :type name: str
    :param object_id:
    :type object_id: str
    :param peeled_object_id:
    :type peeled_object_id: str
    :param statuses:
    :type statuses: list of :class:`GitStatus <git.v4_0.models.GitStatus>`
    :param url:
    :type url: str
    :param repository:
    :type repository: :class:`GitRepository <git.v4_0.models.GitRepository>`
    """

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'is_locked': {'key': 'isLocked', 'type': 'bool'},
        'is_locked_by': {'key': 'isLockedBy', 'type': 'IdentityRef'},
        'name': {'key': 'name', 'type': 'str'},
        'object_id': {'key': 'objectId', 'type': 'str'},
        'peeled_object_id': {'key': 'peeledObjectId', 'type': 'str'},
        'statuses': {'key': 'statuses', 'type': '[GitStatus]'},
        'url': {'key': 'url', 'type': 'str'},
        'repository': {'key': 'repository', 'type': 'GitRepository'}
    }

    def __init__(self, _links=None, is_locked=None, is_locked_by=None, name=None, object_id=None, peeled_object_id=None, statuses=None, url=None, repository=None):
        super(GitForkRef, self).__init__(_links=_links, is_locked=is_locked, is_locked_by=is_locked_by, name=name, object_id=object_id, peeled_object_id=peeled_object_id, statuses=statuses, url=url)
        self.repository = repository



class GitItem(ItemModel):
    """GitItem.

    :param _links:
    :type _links: :class:`ReferenceLinks <git.v4_0.models.ReferenceLinks>`
    :param content_metadata:
    :type content_metadata: :class:`FileContentMetadata <git.v4_0.models.FileContentMetadata>`
    :param is_folder:
    :type is_folder: bool
    :param is_sym_link:
    :type is_sym_link: bool
    :param path:
    :type path: str
    :param url:
    :type url: str
    :param commit_id: SHA1 of commit item was fetched at
    :type commit_id: str
    :param git_object_type: Type of object (Commit, Tree, Blob, Tag, ...)
    :type git_object_type: object
    :param latest_processed_change: Shallow ref to commit that last changed this item Only populated if latestProcessedChange is requested May not be accurate if latest change is not yet cached
    :type latest_processed_change: :class:`GitCommitRef <git.v4_0.models.GitCommitRef>`
    :param object_id: Git object id
    :type object_id: str
    :param original_object_id: Git object id
    :type original_object_id: str
    """

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'content_metadata': {'key': 'contentMetadata', 'type': 'FileContentMetadata'},
        'is_folder': {'key': 'isFolder', 'type': 'bool'},
        'is_sym_link': {'key': 'isSymLink', 'type': 'bool'},
        'path': {'key': 'path', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'},
        'commit_id': {'key': 'commitId', 'type': 'str'},
        'git_object_type': {'key': 'gitObjectType', 'type': 'object'},
        'latest_processed_change': {'key': 'latestProcessedChange', 'type': 'GitCommitRef'},
        'object_id': {'key': 'objectId', 'type': 'str'},
        'original_object_id': {'key': 'originalObjectId', 'type': 'str'}
    }

    def __init__(self, _links=None, content_metadata=None, is_folder=None, is_sym_link=None, path=None, url=None, commit_id=None, git_object_type=None, latest_processed_change=None, object_id=None, original_object_id=None):
        super(GitItem, self).__init__(_links=_links, content_metadata=content_metadata, is_folder=is_folder, is_sym_link=is_sym_link, path=path, url=url)
        self.commit_id = commit_id
        self.git_object_type = git_object_type
        self.latest_processed_change = latest_processed_change
        self.object_id = object_id
        self.original_object_id = original_object_id



class GitPullRequestStatus(GitStatus):
    """GitPullRequestStatus.

    :param _links: Reference links.
    :type _links: :class:`ReferenceLinks <git.v4_0.models.ReferenceLinks>`
    :param context: Context of the status.
    :type context: :class:`GitStatusContext <git.v4_0.models.GitStatusContext>`
    :param created_by: Identity that created the status.
    :type created_by: :class:`IdentityRef <git.v4_0.models.IdentityRef>`
    :param creation_date: Creation date and time of the status.
    :type creation_date: datetime
    :param description: Status description. Typically describes current state of the status.
    :type description: str
    :param id: Status identifier.
    :type id: int
    :param state: State of the status.
    :type state: object
    :param target_url: URL with status details.
    :type target_url: str
    :param updated_date: Last update date and time of the status.
    :type updated_date: datetime
    :param iteration_id: ID of the iteration to associate status with. Minimum value is 1.
    :type iteration_id: int
    """

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'context': {'key': 'context', 'type': 'GitStatusContext'},
        'created_by': {'key': 'createdBy', 'type': 'IdentityRef'},
        'creation_date': {'key': 'creationDate', 'type': 'iso-8601'},
        'description': {'key': 'description', 'type': 'str'},
        'id': {'key': 'id', 'type': 'int'},
        'state': {'key': 'state', 'type': 'object'},
        'target_url': {'key': 'targetUrl', 'type': 'str'},
        'updated_date': {'key': 'updatedDate', 'type': 'iso-8601'},
        'iteration_id': {'key': 'iterationId', 'type': 'int'}
    }

    def __init__(self, _links=None, context=None, created_by=None, creation_date=None, description=None, id=None, state=None, target_url=None, updated_date=None, iteration_id=None):
        super(GitPullRequestStatus, self).__init__(_links=_links, context=context, created_by=created_by, creation_date=creation_date, description=description, id=id, state=state, target_url=target_url, updated_date=updated_date)
        self.iteration_id = iteration_id



class GitPush(GitPushRef):
    """GitPush.

    :param _links:
    :type _links: :class:`ReferenceLinks <git.v4_0.models.ReferenceLinks>`
    :param date:
    :type date: datetime
    :param push_correlation_id:
    :type push_correlation_id: str
    :param pushed_by:
    :type pushed_by: :class:`IdentityRef <git.v4_0.models.IdentityRef>`
    :param push_id:
    :type push_id: int
    :param url:
    :type url: str
    :param commits:
    :type commits: list of :class:`GitCommitRef <git.v4_0.models.GitCommitRef>`
    :param ref_updates:
    :type ref_updates: list of :class:`GitRefUpdate <git.v4_0.models.GitRefUpdate>`
    :param repository:
    :type repository: :class:`GitRepository <git.v4_0.models.GitRepository>`
    """

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'date': {'key': 'date', 'type': 'iso-8601'},
        'push_correlation_id': {'key': 'pushCorrelationId', 'type': 'str'},
        'pushed_by': {'key': 'pushedBy', 'type': 'IdentityRef'},
        'push_id': {'key': 'pushId', 'type': 'int'},
        'url': {'key': 'url', 'type': 'str'},
        'commits': {'key': 'commits', 'type': '[GitCommitRef]'},
        'ref_updates': {'key': 'refUpdates', 'type': '[GitRefUpdate]'},
        'repository': {'key': 'repository', 'type': 'GitRepository'}
    }

    def __init__(self, _links=None, date=None, push_correlation_id=None, pushed_by=None, push_id=None, url=None, commits=None, ref_updates=None, repository=None):
        super(GitPush, self).__init__(_links=_links, date=date, push_correlation_id=push_correlation_id, pushed_by=pushed_by, push_id=push_id, url=url)
        self.commits = commits
        self.ref_updates = ref_updates
        self.repository = repository



class GitTargetVersionDescriptor(GitVersionDescriptor):
    """GitTargetVersionDescriptor.

    :param version: Version string identifier (name of tag/branch, SHA1 of commit)
    :type version: str
    :param version_options: Version options - Specify additional modifiers to version (e.g Previous)
    :type version_options: object
    :param version_type: Version type (branch, tag, or commit). Determines how Id is interpreted
    :type version_type: object
    :param target_version: Version string identifier (name of tag/branch, SHA1 of commit)
    :type target_version: str
    :param target_version_options: Version options - Specify additional modifiers to version (e.g Previous)
    :type target_version_options: object
    :param target_version_type: Version type (branch, tag, or commit). Determines how Id is interpreted
    :type target_version_type: object
    """

    _attribute_map = {
        'version': {'key': 'version', 'type': 'str'},
        'version_options': {'key': 'versionOptions', 'type': 'object'},
        'version_type': {'key': 'versionType', 'type': 'object'},
        'target_version': {'key': 'targetVersion', 'type': 'str'},
        'target_version_options': {'key': 'targetVersionOptions', 'type': 'object'},
        'target_version_type': {'key': 'targetVersionType', 'type': 'object'}
    }

    def __init__(self, version=None, version_options=None, version_type=None, target_version=None, target_version_options=None, target_version_type=None):
        super(GitTargetVersionDescriptor, self).__init__(version=version, version_options=version_options, version_type=version_type)
        self.target_version = target_version
        self.target_version_options = target_version_options
        self.target_version_type = target_version_type
