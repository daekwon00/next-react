import React from 'react';

function UserDetail({ user }) {
  return (
    <div className="user-detail">
      <h2>사용자 정보</h2>
      <div className="user-info">
        <p><strong>ID:</strong> {user.id}</p>
        <p><strong>이름:</strong> {user.name}</p>
        <p><strong>이메일:</strong> {user.email}</p>
      </div>
    </div>
  );
}

export default UserDetail; 