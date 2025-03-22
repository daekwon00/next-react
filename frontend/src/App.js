import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './App.css';
import UserDetail from './components/UserDetail';
import UserForm from './components/UserForm';

function App() {
  const [user, setUser] = useState(null);
  const [userId, setUserId] = useState('1');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const fetchUser = async (id) => {
    setLoading(true);
    setError(null);
    try {
      const response = await axios.get(`/api/users/${id}`);
      setUser(response.data);
    } catch (err) {
      setError('사용자 정보를 불러오는데 실패했습니다.');
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  const updateUser = async (userData) => {
    setLoading(true);
    setError(null);
    try {
      const response = await axios.put(`/api/users/${userId}`, userData);
      setUser(response.data);
      alert('사용자 정보가 업데이트되었습니다.');
    } catch (err) {
      setError('사용자 정보 업데이트에 실패했습니다.');
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchUser(userId);
  }, [userId]);

  return (
    <div className="App">
      <header className="App-header">
        <h1>사용자 관리 시스템</h1>
      </header>
      <main>
        <div className="user-selector">
          <label htmlFor="user-select">사용자 선택: </label>
          <select 
            id="user-select"
            value={userId} 
            onChange={(e) => setUserId(e.target.value)}
          >
            <option value="1">홍길동</option>
            <option value="2">김철수</option>
          </select>
          <button onClick={() => fetchUser(userId)}>조회</button>
        </div>

        {loading && <p>로딩 중...</p>}
        {error && <p className="error">{error}</p>}
        
        {user && (
          <div className="user-container">
            <UserDetail user={user} />
            <UserForm user={user} onSubmit={updateUser} />
          </div>
        )}
      </main>
    </div>
  );
}

export default App; 